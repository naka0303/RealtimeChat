import json
import datetime
from . import models
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
#from asgiref.sync import async_to_sync  # async_to_sync() : 非同期関数を同期的に実行する際に使用する。

# ChatConsumerクラス: WebSocketからの受け取ったものを処理するクラス
class ChatConsumer( AsyncWebsocketConsumer ):

    # WebSocket接続時の処理
    async def connect( self ):
        # グループに参加
        self.strGroupName = 'chat'
        await self.channel_layer.group_add(
            self.strGroupName, self.channel_name
        )

        # WebSocket接続を受け入れます。
        # ・connect()でaccept()を呼び出さないと、接続は拒否されて閉じられます。
        # 　たとえば、要求しているユーザーが要求されたアクションを実行する権限を持っていないために、接続を拒否したい場合があります。
        # 　接続を受け入れる場合は、connect()の最後のアクションとしてaccept()を呼び出します。
        await self.accept()

    # WebSocket切断時の処理
    async def disconnect(self, close_code):
        # グループから離脱
        await self.channel_layer.group_discard(self.strGroupName, self.channel_name)

    # WebSocketからのデータ受信時の処理
    # （ブラウザ側のJavaScript関数のsocketChat.send()の結果、WebSocketを介してデータがChatConsumerに送信され、本関数で受信処理します）
    async def receive(self, text_data):
        # 受信データをJSONデータに復元
        text_data_json = json.loads(text_data)

        # メッセージの取り出し
        strMessage = text_data_json['message']
        chatroom_no, icon, username, message = strMessage.split()
        register_datetime = datetime.datetime.now()
        register_datetime_tostr = register_datetime.strftime('%Y年%m月%d日 %H:%M:%S')

        await self.register_chat_message(chatroom_no, icon, username, message, register_datetime)

        # グループ内の全コンシューマーにメッセージ拡散送信（受信関数を'type'で指定）
        data = {
            'type': 'chat_message', # 受信処理関数名
            'icon': icon,
            'username': username,
            'message': message,
            'register_datetime': register_datetime_tostr
        }
        await self.channel_layer.group_send(self.strGroupName, data)

    # 拡散メッセージ受信時の処理
    # （self.channel_layer.group_send()の結果、グループ内の全コンシューマーにメッセージ拡散され、各コンシューマーは本関数で受信処理します）
    async def chat_message(self, data):
        data_json = {
            'icon': data['icon'],
            'username': data['username'],
            'message': data['message'],
            'register_datetime': data['register_datetime'],
        }

        # WebSocketにメッセージを送信します。
        # （送信されたメッセージは、ブラウザ側のJavaScript関数のsocketChat.onmessage()で受信処理されます）
        # JSONデータをテキストデータにエンコードして送ります。
        await self.send(text_data=json.dumps(data_json))
    
    @database_sync_to_async
    def register_chat_message(self, chatroom_no, icon, username, message, register_datetime):
        try:
            # チャットメッセージをDBに登録
            models.ChatRoomContent.objects.create(
                chatroom_no=chatroom_no,
                icon=icon,
                username=username,
                message=message,
                register_datetime=register_datetime
            )
        except Exception as err:
            raise Exception(err)
