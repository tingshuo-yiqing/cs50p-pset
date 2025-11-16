class Word:
    def __init__(self, word, Chinese, correct_count=0, error_count=0):
        self.word = word
        self.Chinese = Chinese
        self.correct_count = correct_count
        self.error_count = error_count
    
    def __str__(self):
        return f"{self.Chinese}: {self.word}"

    def to_dict(self):
        """Word -> dict"""
        return {
            "Word": self.word,
            "Chinese": self.Chinese,
            "correct_count": self.correct_count,
            "error_count": self.error_count
        }
    
    @classmethod   #* 类方法是什么？为什么用类方法
    def from_dict(cls, data):
        """dict -> Word"""
        return cls(
            data.get("Word", ""),  #* 这里为什么要为空
            data.get("Chinese", ""),
            data.get("correct_count", 0),
            data.get("error_count", 0)
        )