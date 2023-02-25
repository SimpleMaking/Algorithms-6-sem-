
class Queue:
    def __init__(self, elems=None):
        try:
            self.__queue = list(elems)
        except Exception:
            self.__queue = list()
        self.obj = self.__queue
        self.iter_obj = iter(self.__queue) 
       
    def __iter__(self):
        self.counter = 0
        return self    
    
    def __next__(self):
            if self.counter < len(self.__queue):
                result = next(self.iter_obj)
                self.counter += 1
                return result
            else:
                self.counter = 0
                self.iter_obj = iter(self.obj)
                raise StopIteration
            
    def add(self, elem):
        self.__queue.insert(len(self.__queue), elem)
        
    def remove(self):
        return self.__queue.pop(0)
    
    def size(self):
        return len(self.__queue)
    
    def is_void(self):
        if len(self.__queue):
            return False
        else:
            return True
    
    def get_queue(self):
        return self.__queue
    
    def get_elem(self, index):
        return self.__queue[index]
    
    
import random
import datetime

def test_1():
    que = Queue()
    for i in range(0, 1000):
        que.add(random.randint(-1000, 1000))
    
    max = que.get_elem(0); min = max; avg = 0
    for value in que:
        if value > max:
            max = value
        if value < min:
            min = value
        avg += value
    
    sum = avg
    avg //= que.size()
    print(f"test 1:  max: {max}, min: {min}, avg: {avg}, sum {sum}")


def test_2():
    que = Queue()
    counter = 0
    for i in range(0, 10):
        que.add(f"string {counter}")
        counter += 1
    
    print("Исходная очередь", )
    for value in que:
        print(value, end=" ")
    print("\n")
    que.add("Hey brother!")
    print("Очередь после добавления элемента")
    for value in que:
        print(value, end=" ")
    print("\n")
    que.remove()
    print("Очередь после удаления элемента")
    for value in que:
        print(value, end=" ")
    print("\n")
       
def test_3():
    l = list()
    name = ["Leo", "Vova", "Andrey"]
    second_name = ["Kazantsev", "Ivanov", "Sidorov"]
    third_name = ["Anatolich", "Bubich", "Petrovich"]
    date = [datetime.datetime(1980, 1, 1), datetime.datetime(1990, 5, 1),datetime.datetime(2020, 1, 1)]
    for i in range(0, 100):
        que = Queue()
        que.add(random.choice(name))
        que.add(random.choice(second_name))
        que.add(random.choice(third_name))
        que.add(random.choice(date))
        l.append(que)
        
    l_ = list()
    l__ = list()
    counter_for_20 = 0
    counter_for_30 = 0
    que_ = Queue()
    for value in l:
        if ((datetime.datetime.now() - value.get_elem(3)).days / 365) < 20:
            l_.append(value)
            counter_for_20 += 1
        elif ((datetime.datetime.now() - value.get_elem(3)).days / 365) > 30: 
            l__.append(value)
            counter_for_30 += 1
    print(f"Количество людей старше 30 лет: {counter_for_30}")
    print(f"Количество людей младше 20 лет: {counter_for_20}")
    print(f"Количество людей, не попавших ни в одну категорию: {len(l) - (counter_for_30 + counter_for_20)}")
            

def test_4():
    que = Queue()
    for i in range(0, 1000):
        que.add(random.randint(-1000, 1000))
        
    print(f"Первые 10 элементов для примера")
    counter = 0
    for value in que:
        if counter != 10:
            print(value, end=" ")
        else:
            break
        counter += 1
    print("\n")    
    que = sorted(que.get_queue())
    print(f"Отсортированные первые 10 элементов для примера")
    counter = 0
    for value in que:
        if counter != 10:
            print(value, end=" ")
        else:
            break
        counter += 1
    print("\n")

def test_5():
    que = Queue()
    for i in range(0, 10):
        que.add(random.randint(-1000, 1000))
    print("Заполенная очередь")
    for value in que:  
        print(value, end=" ")
    print("\n")
    que = sorted(que.get_queue()) 
    print("Отсортированная очередь")
    for value in que:  
        print(value, end=" ")
    print("\n") 
    sorted_que = Queue(que)
    inverted_que = Queue()
    for i in range(len(sorted_que.get_queue()) - 1, -1, -1):
        elem = sorted_que.get_elem(i)
        inverted_que.add(elem)
    print("Инверсированная очередь")
    for value in inverted_que:
        print(value, end=" ")    
    print("\n")
    
# test_1()
# test_2()
# test_3()
# test_4()
test_5()    