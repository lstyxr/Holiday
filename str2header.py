def Str2Header(header_raw):
    if header_raw is None:
        return None
    # 按行分割处理成列表，有几行就生成几个元素，
    # 如['Accept: */*', 'Accept-Encoding: gzip, deflate, br', ...]
    headers = header_raw.splitlines()
    # 继续将列表按冒号“:”分割处理成由多个列表组合成一个总列表,嵌套列表:[[]]
    # 例：[['Accept', ' */*'], ['Accept-Encoding', ' gzip, deflate, br'], ...]
    headers_tuples = [header.split(':', 1) for header in headers]

    result_dict = {}
    for header_item in headers_tuples:
        # 判断列表是否含有2个元素，
        # 即像这样的：['Accept', ' */*']
        # 不含2个元素的是无效条目，用continue忽略
        if not len(header_item) == 2:
            continue

        item_key = header_item[0].strip()
        item_value = header_item[1].strip()

        result_dict[item_key] = item_value
    return result_dict


if __name__ == '__main__':
    test = Str2Header('Accept: application/json, text/javascript, */*; q=0.01')
    print(test)