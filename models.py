class Users:
    def __init__(self, username='', password='', salt=''):
        self._id = -1
        self.username = username
        self._hashed_password = hash_password(password, salt)

    @property
    def id(self):
        return self._id

    # udostępnić na zewnątrz klasy własności _id

    @property
    def hashed_password(self):
        return self._hashed_password

    # udostępnić na zewnątrz klasy własności _hashed_password

    def set_password(self, password, salt=''):
        self._hashed_password = hash_password(password, salt)

    @hashed_password.setter
    def hashed_password(self, password):
        self.set_password(password)

    def save_to_db(self, cursor):
        if self._id == -1:
            sql = """ inset into users (username, hashed_password) values (%s, %s) returning id """
            values(self.username, self.hashed_password)
            cursor.execute(sql, values)  # tu nie musi być przecinek ??
            self._id = cursor.fetchone()[0]  # dlaczego nie fatchall ??
            return True
        return False

    @staticmethod  # funkcja jest statyczna – możemy jej używać na klasie, a nie na obiekcie.
    def load_user_by_id(cursor, id_):
        sql = select
        id, username, hashed_password
        from users where
        id = % S
        cursor.execute(sql, (id_,))
        data = cursor.fetchone()
        if data:
            id_, username, hashed_password = data
            loaded_user = User(username)
            loaded_user._id = id_
            loaded_user._hashed_password = hashed_password
            return loaded_user
        else:
            return None

    @staticmethod
    def load_all_users(cursor):
        pass


class Messages():
    pass
