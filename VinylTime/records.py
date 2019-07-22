def records():
    import json
    try:
        with open('record_collection.json') as handle:
            records = json.loads(handle.read())
    except:
        print('You must have a collection to create a play list!!!!')

    rec_lst = []  

    for i in records.keys():
        for x in records[i].keys():
            if records[i][x]['Sides'] == 1:
                rec_lst.append(i + ' '+ '"' + x + '"'+  ' ' + 'Speed:' + ' ' + str(records[i][x]['Speed']) + ' ' + 'Size:'+ str(records[i][x]['Size'])+ ' '+ 'A')
            if records[i][x]['Sides'] == 2:
                rec_lst.append(i + ' '+ '"' + x + '"'+  ' ' + 'Speed:' + ' ' + str(records[i][x]['Speed']) + ' ' + 'Size:'+ str(records[i][x]['Size'])+ ' '+ 'A')
                rec_lst.append(i + ' '+ '"' + x + '"'+  ' ' + 'Speed:' + ' ' + str(records[i][x]['Speed']) + ' ' + 'Size:'+ str(records[i][x]['Size'])+ ' '+ 'B')
            if records[i][x]['Sides'] == 3:
                rec_lst.append(i + ' '+ '"' + x + '"'+  ' ' + 'Speed:' + ' ' + str(records[i][x]['Speed']) + ' ' + 'Size:'+ str(records[i][x]['Size'])+ ' '+ 'A')
                rec_lst.append(i + ' '+ '"' + x + '"'+  ' ' + 'Speed:' + ' ' + str(records[i][x]['Speed']) + ' ' + 'Size:'+ str(records[i][x]['Size'])+ ' '+ 'B')
                rec_lst.append(i + ' '+ '"' + x + '"'+  ' ' + 'Speed:' + ' ' + str(records[i][x]['Speed']) + ' ' + 'Size:'+ str(records[i][x]['Size'])+ ' '+ 'C')
            if records[i][x]['Sides'] == 4:
                rec_lst.append(i + ' '+ '"' + x + '"'+  ' ' + 'Speed:' + ' ' + str(records[i][x]['Speed']) + ' ' + 'Size:'+ str(records[i][x]['Size'])+ ' '+ 'A')
                rec_lst.append(i + ' '+ '"' + x + '"'+  ' ' + 'Speed:' + ' ' + str(records[i][x]['Speed']) + ' ' + 'Size:'+ str(records[i][x]['Size'])+ ' '+ 'B')
                rec_lst.append(i + ' '+ '"' + x + '"'+  ' ' + 'Speed:' + ' ' + str(records[i][x]['Speed']) + ' ' + 'Size:'+ str(records[i][x]['Size'])+ ' '+ 'C')
                rec_lst.append(i + ' '+ '"' + x + '"'+  ' ' + 'Speed:' + ' ' + str(records[i][x]['Speed']) + ' ' + 'Size:'+ str(records[i][x]['Size'])+ ' '+ 'D')
    
    #print(rec_lst)
    return(rec_lst)
    records.close()
            