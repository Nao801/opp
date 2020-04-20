'''
データ型宣言：UserName
	属性：
		実際のユーザー名
	ルール：
		ユーザー名は4文字以上20文字以下である
	できること=>メソッド
		ユーザー名を大文字に変換する
'''


class UserName:
    def __init__(self, name):
        if not (4 <= len(name) <= 20):
            raise ValueError(f'{name}は文字数のルール違反！')
        self.name = name

    def screen_name(self):
        return self.name.upper()


# UserNameクラスのインスタンス化
hibiki = UserName('hibiki')
# print(hibiki)
# print(type(hibiki))
print(hibiki.name)
'''
sho = UserName('sho')
print(sho.name)
'''
print(hibiki.screen_name())
