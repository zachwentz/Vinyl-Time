def record_collection():
    import json
    try:
        with open('record_collection.json') as handle:
            records = json.loads(handle.read())
    except:
        print('You must have a collection to view a collection!!!!')

    record_col = []  

    for i in records.keys():
        for x in records[i].keys():
            record_col.append(i + ' '+ '"' + x + '"' +  ' ' + 'Sides:' + ' ' + str(records[i][x]['Sides']) +  ' ' + 'Speed:' + ' ' + str(records[i][x]['Speed']) + ' ' + 'Size:'+ str(records[i][x]['Size']))
           
    
    #print(rec_lst)
    return(record_col)
    #record_collection.close()
            

