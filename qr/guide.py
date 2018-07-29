import sys
import re


def get_necessary_data(data):
    data = data.split('\n')
    return data[1]


def main(data: str):
    result = list()
    data = get_necessary_data(data)
    if re.search(r'秋葉原', data):
        if re.search(r'ワークショップ', data):
            result.append(re.search(r'ワークショップ\S*', data).group())
            result = ' '.join(result)
            result += 'のご予約ですね。テレビの前のテーブルのお好きなお席におかけください。こちらにいらっしゃるのは初めてですか。'


        elif re.search(r'タッチ.?トライ', data):
            result.append(re.search(r'タッチ.?トライ', data).group())
            result = ' '.join(result)
            result += 'のご予約ですね。スタッフがペッパーをご用意いたしますので、向かって奥のテーブルか右側のテーブルのお好きなお席にかけてお待ちください。'

    sys.stdout.write(result)


if __name__ == '__main__':
    data = sys.argv[1]
    main(data)
