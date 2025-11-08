class Player:
    def __init__(self):
        self.argent = 0
    def mget(self):
        return self.argent
    def madd(self,nbr):
        self.argent += nbr
    def msub(self,nbr) -> bool:
        """
        Return affordability and subtract nbr from money, if false, cancel transaction
        """
        if nbr > self.argent:
            return False
        else:
            self.argent -= nbr
            return True