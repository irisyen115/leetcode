char repeatedCharacter(char * s){
    int length = strlen(s);
    bool appear[26] = {false}; 
    
    for(int i = 0; i < length; i++) {
        if(appear[s[i] - 'a'] == true) {
            return s[i];
        }
        appear[s[i] - 'a'] = true;
    }
    return 'a';
}
