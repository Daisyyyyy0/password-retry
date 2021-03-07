
password = 'qqq123'
i = 3  # 剩餘機會
while i > 0:
    i -= 1
    pw = input('請輸入密碼：')
    if pw == password:
        print('登入成功！')
        break
    else:
        print('密碼錯誤!')
        if i > 0:
            print('密碼錯誤！還有', i, '次機會')
        else:
            print('很抱歉！您已多次嘗試失敗，請聯絡管理者')
