class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        return len(password) >= 8 and any(v.isupper() for v in password) and any(v.islower() for v in password) and any(v.isdigit() for v in password) and any(v in "!@#$%^&*()-+" for v in password) and all(len(list(y)) < 2 for x, y in itertools.groupby(password))
        