student_data = {'id':
    {'name': ['Sara'],
     'class' : ['V'],
     'subject_integration' : ['English, Math, Science']
    },
    'id2':
    {'name' : 'Dave',
     'class' : ['V'],
     'subject_integration' : ['English, Math, Science']
    },
    'id3':
    {'name': ['Sara'],
     'class' : ['V'],
     'subject_integration' : ['English, Math, Science']
    },
    'id4':
    {'name' : ['John'],
     'class' : ['V'],
     'subject_integration' : ['English, Math, Science']
    }, 
}

results = {}

for key,value in student_data.items():
    if value not in results.values():
        results[key] = value

print(results)