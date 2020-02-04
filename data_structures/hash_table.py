from .prime_num_util import find_next_prime


class HashTable:

    def __init__(self, size):
        self.size = size
        self.values = [None] * self.size
        self.limit_charge = 0.75

    def balanced_factor(self):
        pass

    def hash_code(self, key):
        return key % self.size

    def insert(self, v):
        key = self.hash_code(v)
        if self.values[key] is not None:
            self._set_value(key, v)
        # 解决Hash冲突
        elif self.values[key] != v:
            key = self._collision_resolve(key, v)
            if key:
                self._set_value(key, v)
            # 重建散列表再插入数据
            else:
                self.rehashing()
                self.insert(v)

    def rehashing(self):
        survivor = [x for x in self.values if x is not None]
        self.size = find_next_prime(self.size, factor=2)
        self.values = [None] * self.size
        return [self.insert(x) for x in survivor]

    def _set_value(self, k, v):
        self.values[k] = v

    # 返回 None代表Hash表满了，需要重建
    def _collision_resolve(self, key, v):
        new_key = self.hash_code(key + 1)

        while self.values[new_key] is not None:
            if self.values.count(None) > 0:
                new_key = self.hash_code(new_key + 1)
            else:
                return None
        return new_key

