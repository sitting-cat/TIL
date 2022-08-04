all_pages = 500
done_pages = list()

try:
    done_pages.append(int(input()))
    done_pages.append(int(input()))
    done_pages.append(int(input()))
    done_pages.append(int(input()))    
    done_pages.append(int(input()))    
except ValueError as e:
    raise ValueError("半角数値以外が入力されました") from e

remain_pages: int = all_pages - sum(done_pages)
print(remain_pages)
