import os

notePath = r'D:/KnowDo/Book Notes/0 My Clippings.txt'
digestPath = 'D:/KnowDo/Book Notes/digest/'

# 确保目录存在
if not os.path.exists(digestPath):
    os.makedirs(digestPath)

with open(notePath, 'r', encoding='utf-8') as f:
    while True:  # 无限循环
        oneNote = []  # 设置用于储存的onenote
        while True:  # 对于单个书签的读取，也设置为无限循环，遇到特定字符停止
            line = f.readline()  # 读取每一行
            oneNote.append(line)  # 添加到onenote
            if ('==========' in line) | (not line):  # 遇到特定字符停止
                break
        if not line:
            break

        # 使用 .format() 方法格式化字符串
        bookName = oneNote[0].strip()  # 移除可能的前后空白字符
        bookPath = os.path.join(digestPath, f"{bookName}.txt")

        with open(bookPath, 'a+', encoding='utf-8') as bookNote:
            for i in range(len(oneNote) - 4):
                bookNote.write(oneNote[3 + i])  # 写入第四行内容，并自动换行
            bookNote.write('\n')
