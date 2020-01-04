# 展开嵌套的列表

# 递归和非递归方法演示

def list_or_tuple(x):  
      return isinstance(x, (list, tuple))  
      
def flatten(sequence, to_expand=list_or_tuple):  
      for item in sequence:  
            if to_expand(item):  
                  for subitem in flatten(item, to_expand):  
                        yield subitem  
            else:  
                  yield item 


def flatten(sequence, to_expand=list_or_tuple):  
      iterators = [ iter(sequence) ]  
      while iterators:  
            # 循环当前的最深嵌套（最后）的迭代器  
            for item in iterators[-1]:  
                  if to_expand(item):  
                        # 找到了子序列，循环子序列的迭代器  
                        iterators.append(iter(item))  
                        break  
                  else:  
                        yield item  
            else:  
                  # 最深嵌套的迭代器耗尽，回过头来循环它的父迭代器  
                  iterators.pop( ) 
