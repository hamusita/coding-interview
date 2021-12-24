class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyDict:
    def __init__(self):
        self.table = [None] * 1000

    def hash(self, key):
        # 1000で割った余りをhash値として扱う
        return key % 1000

    def add(self, key, value):
        hashed_key = self.hash(key)
        if self.table[hashed_key]:  # すでにキーにデータが存在したら
            ll = self.table[hashed_key]  # すでに存在しているデータ(連結リストの先頭)
            while ll:  # 連結リストの最後尾までループして，最後にデータを追加する
                if not ll.next:  # 連結リストの最後の場合
                    ll.next = LinkedList(value)  # 新しい値を連結リストに連結
                    break
                else:
                    ll = ll.next
        else:
            self.table[hashed_key] = LinkedList(value)  # データが既に存在していない場合，連結リストとしてデータを挿入

    def get(self, key):
        values = []
        hashed_key = self.hash(key)
        ll = self.table[hashed_key]
        if not ll:
            return -1
        while ll:
            values.append(ll.value)
            if not ll.next:
                return values
            else:
                ll = ll.next

    def remove(self, key, value):
        hashed_key = self.hash(key)
        ll = self.table[hashed_key]
        if not ll:
            print('No Data')
            return
        if ll.value == value:
            if ll.next:
                self.table[hashed_key] = ll.next
            else:
                self.table[hashed_key] = None
            print(f'Key:{key}, Value:{value} Removed')
            return
        ll_prev = ll
        ll = ll_prev.next
        while ll:
            if ll.value == value:
                ll_prev.next = ll.next
                print(f'Key:{key}, Value:{value} Removed')
                return
            else:
                ll_prev = ll
                ll = ll.next
        print('Data not Found')
