
password = 'qqq123'
i = 3  # 剩餘機會
while True:
    pw = input('請輸入密碼：')
    if pw == password:
        print('登入成功！')
        break
    else:
        i -= 1
        print('密碼錯誤！密碼錯誤！還有', i, '次機會')
        if i <= 0:
            break
