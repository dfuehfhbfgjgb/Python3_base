function $(tag,index){
    var elems = document.getElementsByTagName(tag);
    if(index){        
        return elems[index];
    }else{//index为0或者undefined时
        return elems[0];
    }        
}

