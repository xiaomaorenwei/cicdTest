# library.py
# 图书馆类定义文件

import json
import os
from datetime import datetime
from book import Book

class Library:
    """图书馆类，用于管理图书的增删改查和借阅"""
    
    def __init__(self, data_file="books.json"):
        """初始化图书馆对象
        
        参数:
            data_file (str): 数据文件路径，默认为'books.json'
        """
        self.data_file = data_file
        self.books = {}
        self.load_data()
    
    def load_data(self):
        """从文件加载图书数据"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for book_id, book_data in data.items():
                        self.books[book_id] = Book.from_dict(book_data)
                print(f"已从{self.data_file}加载{len(self.books)}本图书")
            except Exception as e:
                print(f"加载数据时出错: {e}")
                self.books = {}
        else:
            print("未找到数据文件，将创建新的数据文件")
            self.books = {}
    
    def save_data(self):
        """保存图书数据到文件"""
        try:
            data = {book_id: book.to_dict() for book_id, book in self.books.items()}
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"数据已保存到{self.data_file}")
            return True
        except Exception as e:
            print(f"保存数据时出错: {e}")
            return False
    
    def add_book(self, book):
        """添加图书
        
        参数:
            book (Book): 要添加的图书对象
            
        返回:
            bool: 是否添加成功
        """
        if book.book_id in self.books:
            print(f"图书ID {book.book_id} 已存在")
            return False
        
        self.books[book.book_id] = book
        print(f"已添加图书: {book}")
        self.save_data()
        return True
    
    def remove_book(self, book_id):
        """删除图书
        
        参数:
            book_id (str): 要删除的图书ID
            
        返回:
            bool: 是否删除成功
        """
        if book_id not in self.books:
            print(f"图书ID {book_id} 不存在")
            return False
        
        book = self.books.pop(book_id)
        print(f"已删除图书: {book}")
        self.save_data()
        return True
    
    def get_book(self, book_id):
        """获取图书
        
        参数:
            book_id (str): 图书ID
            
        返回:
            Book: 图书对象，如果不存在则返回None
        """
        return self.books.get(book_id)
    
    def search_books(self, keyword):
        """搜索图书
        
        参数:
            keyword (str): 搜索关键词，可以匹配ID、标题、作者或出版社
            
        返回:
            list: 匹配的图书对象列表
        """
        keyword = keyword.lower()
        results = []
        
        for book in self.books.values():
            if (keyword in book.book_id.lower() or
                keyword in book.title.lower() or
                keyword in book.author.lower() or
                keyword in book.publisher.lower()):
                results.append(book)
        
        return results
    
    def list_all_books(self):
        """列出所有图书
        
        返回:
            list: 所有图书对象的列表
        """
        return list(self.books.values())
    
    def borrow_book(self, book_id, borrower):
        """借阅图书
        
        参数:
            book_id (str): 图书ID
            borrower (str): 借阅人姓名
            
        返回:
            bool: 是否借阅成功
        """
        book = self.get_book(book_id)
        if not book:
            print(f"图书ID {book_id} 不存在")
            return False
        
        if book.status != "可借阅":
            print(f"图书 '{book.title}' 已被借出，无法借阅")
            return False
        
        book.status = "已借出"
        book.borrower = borrower
        book.borrow_date = datetime.now().strftime("%Y-%m-%d")
        print(f"图书 '{book.title}' 已借给 {borrower}")
        self.save_data()
        return True
    
    def return_book(self, book_id):
        """归还图书
        
        参数:
            book_id (str): 图书ID
            
        返回:
            bool: 是否归还成功
        """
        book = self.get_book(book_id)
        if not book:
            print(f"图书ID {book_id} 不存在")
            return False
        
        if book.status != "已借出":
            print(f"图书 '{book.title}' 未被借出，无需归还")
            return False
        
        borrower = book.borrower
        book.status = "可借阅"
        book.borrower = None
        book.borrow_date = None
        print(f"图书 '{book.title}' 已由 {borrower} 归还")
        self.save_data()
        return True
    
    def get_recent_books(self, count=5):
        """获取最近添加的图书
        
        参数:
            count (int): 返回的图书数量，默认为5
            
        返回:
            list: 最近添加的图书对象列表
        """
        return list(self.books.values())[-count:]