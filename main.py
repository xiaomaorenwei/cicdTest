# main.py
# 图书管理系统主程序

import os
import sys
from book import Book
from library import Library
print("hello,world")
print("hello,world")
print("hello,world")

class LibrarySystem:
    """图书管理系统，提供命令行界面"""
    
    def __init__(self):
        """初始化图书管理系统"""
        self.library = Library()
        self.menu_options = {
            "1": self.add_book,
            "2": self.remove_book,
            "3": self.search_books,
            "4": self.list_all_books,
            "5": self.borrow_book,
            "6": self.return_book,
            "0": self.exit_system
        }
    
    def display_menu(self):
        """显示主菜单"""
        print("\n===== 图书管理系统 =====")
        print("1. 添加图书")
        print("2. 删除图书")
        print("3. 搜索图书")
        print("4. 显示所有图书")
        print("5. 借阅图书")
        print("6. 归还图书")
        print("0. 退出系统")
        print("======================\n")
    
    def run(self):
        """运行图书管理系统"""
        print("欢迎使用图书管理系统！")
        while True:
            self.display_menu()
            choice = input("请输入选项: ")
            action = self.menu_options.get(choice)
            if action:
                action()
            else:
                print("无效选项，请重新输入")
    
    def add_book(self):
        """添加图书"""
        print("\n----- 添加图书 -----")
        book_id = input("请输入图书ID: ")
        title = input("请输入书名: ")
        author = input("请输入作者: ")
        publisher = input("请输入出版社: ")
        
        book = Book(book_id, title, author, publisher)
        self.library.add_book(book)
    
    def remove_book(self):
        """删除图书"""
        print("\n----- 删除图书 -----")
        book_id = input("请输入要删除的图书ID: ")
        self.library.remove_book(book_id)
    
    def search_books(self):
        """搜索图书"""
        print("\n----- 搜索图书 -----")
        keyword = input("请输入搜索关键词: ")
        results = self.library.search_books(keyword)
        
        if results:
            print(f"\n找到 {len(results)} 本匹配的图书:")
            for i, book in enumerate(results, 1):
                print(f"{i}. {book}")
        else:
            print("未找到匹配的图书")
    
    def list_all_books(self):
        """列出所有图书"""
        print("\n----- 所有图书 -----")
        books = self.library.list_all_books()
        
        if books:
            print(f"共有 {len(books)} 本图书:")
            for i, book in enumerate(books, 1):
                print(f"{i}. {book}")
        else:
            print("图书馆中没有图书")
    
    def borrow_book(self):
        """借阅图书"""
        print("\n----- 借阅图书 -----")
        book_id = input("请输入要借阅的图书ID: ")
        borrower = input("请输入借阅人姓名: ")
        self.library.borrow_book(book_id, borrower)
    
    def return_book(self):
        """归还图书"""
        print("\n----- 归还图书 -----")
        book_id = input("请输入要归还的图书ID: ")
        self.library.return_book(book_id)
    
    def exit_system(self):
        """退出系统"""
        print("\n感谢使用图书管理系统，再见！")
        sys.exit(0)


if __name__ == "__main__":
    # 清屏
    os.system('cls' if os.name == 'nt' else 'clear')
    # 运行系统
    system = LibrarySystem()
    system.run()