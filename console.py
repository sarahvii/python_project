import pdb
from models.munro import Munro
from models.hiker import Hiker
from models.todo import Todo
import repositories.munro_repository as munro_repository
import repositories.hiker_repository as hiker_repository
import repositories.todo_repository as todo_repository

# munro_repository.delete_all()
# hiker_repository.delete_all()
# todo_repository.delete_all()

hiker1 = Hiker("Gemma", 34)
hiker_repository.save(hiker1)

hiker2 = Hiker("George", 95)
hiker_repository.save(hiker2)

munro1 = Munro("Ben One", 1024)
munro_repository.save(munro1)

munro2 = Munro("Ben Two", 1500)
munro_repository.save(munro2)

todo1 = Todo(hiker1, munro2)
todo_repository.save(todo1)

result = munro_repository.select_all()
hiker_result = hiker_repository.select_all()

for munro in result:
    print(munro.__dict__)

for hiker in hiker_result:
    print(hiker.__dict__)

# pdb.set_trace()

