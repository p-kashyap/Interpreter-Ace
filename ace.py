"""##########################
# Constants #"""
digits='0123456789'
"""##########################"""
TT_INT='INT'
TT_FLOAT='FLOAT'
TT_PLUS='PLUS'
TT_MINUS='MINUS'
TT_MUL='MUL'
TT_DIV='DIV'
TT_LPAREN='LPAREN'
TT_RPAREN='RPAREN'
"""#########################
   #########ERROR###########
   #########################"""
class Error:
    def __init__(self,name,deats):
        self.deats=deats
        self.name=name
    def __repr__(self):
        return f'{self.name}:{self.deats}'
class IllegalChar(Error):
    def __init__(self, deats):
        super().__init__("Illegal Character",deats)
"""#######################
  ########TOKEN###########
  #######################"""
class Token:
    def __init__(self,type,value=None):
        self.type=type
        self.value=value
    def __repr__(self):#repr method calls function __repr__ which returns a string containing a printable representation of an object 
        if self.value:return f'{self.type}:{self.value}'
        return f'{self.type}'
"""##########################################
#####################PARSER##################
#############################################"""
class parser():
    def __init__(self,tokens):
        self.tokens=tokens
        self.idx=-1
        self.advance()
    def advance(self):
        self.idx+=1
        if self.idx<len(self.tokens):
            self.curr_tok=self.tokens[self.idx]
        return self.curr_tok
    def parse(self):
        res=self.expr
        return res
    def factor(self):
        if self.curr_tok.type in (TT_INT,TT_FLOAT):
            self.advance()
            return NumberNode(self.curr_tok)
    def term(self):
        return self.bin_op(self.factor,(TT_MUL,TT_DIV))
    def expr(self):
        return self.bin_op(self.term,(TT_PLUS,TT_MINUS))
    def bin_op(self,func,ops):
        left=func()
        while self.curr_tok.type in ops:
            op_tok=self.curr_tok
            self.advance()
            right=func()
            left=BinOpNode(left,op_tok,right)
        return left
class NumberNode:
    def __init__(self,tok):
        self.tok=tok
    def __repr__(self):
        return f'{self.tok}'
class BinOpNode:
    def __init__(self,left_tok,right_tok,op):
        self.left_node=left_tok
        self.op_tok=op
        self.right_node=right_tok
    def __repr__(self):
        return f'({self.left_node,self.op_tok,self.right_node})'
    
"""###############################################
##################LEXER########################
###############################################"""
class lexer:
    def __init__(self,text):
        self.text=text
        self.pos=-1
        self.curr_char=None
        self.advance()
    def advance(self):
        self.pos+=1
        self.curr_char=self.text[self.pos] if self.pos<len(self.text) else None
    def make_token(self):
        tokens=[]
        while self.curr_char!=None:
            if self.curr_char ==" ":
                self.advance()
            elif self.curr_char in digits:
                tokens.append(self.make_number())
            elif self.curr_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.curr_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.curr_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.curr_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.curr_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.curr_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
            else:
                char =self.curr_char
                self.advance()
                return [],IllegalChar("'"+char+"'")
        return tokens,None

    def make_number(self):
        dotcount=0
        num_str=""
        while self.curr_char and self.curr_char in digits or self.curr_char==".":
            if self.curr_char==".":
                if dotcount==1:
                    break
                dotcount+=1
                num_str+=self.curr_char
            else:
                num_str+=self.curr_char
            self.advance()
        if dotcount==0:
            return Token(TT_INT,int(num_str))
        else:
            return Token(TT_FLOAT,float(num_str))
"""#############################
 #############RUN###############
 ##############################"""
def Run(text):
    l=lexer(text)
    tokens,Error=l.make_token()
    p=parser(tokens)
    ast=p.parse()
    return ast,None



            
