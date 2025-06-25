# book.py
# 图书类定义文件

class Book:
    """图书类，用于表示图书的基本信息"""
    
    def __init__(self, book_id, title, author, publisher, status="可借阅"):
        """初始化图书对象
        
        参数:
            book_id (str): 图书ID
            title (str): 图书标题
            author (str): 作者
            publisher (str): 出版社
            status (str): 图书状态，默认为'可借阅'
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.status = status  # 可借阅/已借出
        self.borrower = None  # 借阅人
        self.borrow_date = None  # 借阅日期
    
    def __str__(self):
        """返回图书信息的字符串表示"""
        return f"ID: {self.book_id}, 书名: {self.title}, 作者: {self.author}, 出版社: {self.publisher}, 状态: {self.status}"
    
    def to_dict(self):
        """将图书对象转换为字典，用于数据存储"""
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "publisher": self.publisher,
            "status": self.status,
            "borrower": self.borrower,
            "borrow_date": self.borrow_date
        }
    
    @classmethod
    def from_dict(cls, data):
        """从字典创建图书对象，用于数据加载
        
        参数:
            data (dict): 包含图书信息的字典
            
        返回:
            Book: 新创建的图书对象
        """
        book = cls(
            data["book_id"],
            data["title"],
            data["author"],
            data["publisher"],
            data["status"]
        )
        book.borrower = data.get("borrower")
        book.borrow_date = data.get("borrow_date")
        return book