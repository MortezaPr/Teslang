
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AS BEGIN BOOLEAN COLON COMMA DBL_COLON DIVIDE DO DOUBLE_EQ DOUBLE_LSQUAREBR DOUBLE_RSQUAREBR ELSE ELSEIF END EQ EXIT FALSE FN FOR GREATER_THAN GREATER_THAN_EQ ID IF INT LCURLYEBR LENGTH LESS_THAN LESS_THAN_EQ LIST LPAREN LSQUAREBR MINUS NOT NOT_EQ NULL NUMBER OR PLUS PRINT QUESTION_MARK RCURLYEBR RETURN RPAREN RSQUAREBR SCAN SEMI_COLON STRING TIMES TO TRUE VECTOR WHILEprog : empty \n                | func progempty :stmt : expr SEMI_COLON\n                | defvar SEMI_COLON\n                | func SEMI_COLON\n                | single_if\n                | else_if\n                | while_loop\n                | for_loop\n                | do_while\n                | return_is SEMI_COLON\n                | blockbody : empty\n            | stmt bodyreturn_is : RETURN exprwhile_loop : WHILE LPAREN expr RPAREN stmtfor_loop : FOR LPAREN ID EQ expr TO expr RPAREN stmtdo_while : DO stmt WHILE DOUBLE_LSQUAREBR expr DOUBLE_RSQUAREBRblock :     BEGIN body ENDsingle_if : IF DOUBLE_LSQUAREBR  expr DOUBLE_RSQUAREBR stmtelse_if : IF DOUBLE_LSQUAREBR expr DOUBLE_RSQUAREBR stmt ELSE stmtdefvar : ID DBL_COLON type\n                    | ID DBL_COLON type EQ exprtype : INT\n                | STRING\n                | VECTOR\n                | NULL\n                | BOOLEANfunc : FN ID LPAREN flist RPAREN LESS_THAN type GREATER_THAN LCURLYEBR body RCURLYEBR\n                | FN ID LPAREN flist RPAREN LESS_THAN type GREATER_THAN EQ GREATER_THAN return_isflist : empty\n                | ID AS type\n                | ID  AS type COMMA flistclist : empty\n                | expr\n                | expr COMMA clistexpr : expr LSQUAREBR expr RSQUAREBR\n                | LSQUAREBR clist RSQUAREBR\n                | expr QUESTION_MARK expr COLON expr\n                | expr PLUS expr\n                | expr MINUS expr\n                | expr TIMES expr\n                | expr DIVIDE expr\n                | expr GREATER_THAN expr\n                | expr LESS_THAN expr\n                | expr DOUBLE_EQ expr\n                | expr GREATER_THAN_EQ expr\n                | expr LESS_THAN_EQ expr\n                | expr NOT_EQ expr\n                | expr AND expr\n                | expr OR expr\n                | NOT expr\n                | PLUS expr\n                | MINUS expr\n                | ID\n                | ID EQ expr\n                | ID LPAREN clist RPAREN\n                | NUMBER\n                | STRING'
    
_lr_action_items = {'$end':([0,1,2,3,5,44,45,56,79,80,81,82,87,89,90,95,96,97,98,99,100,101,102,103,104,105,106,107,114,116,124,],[-3,0,-1,-3,-2,-59,-60,-30,-56,-54,-55,-53,-16,-31,-57,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-39,-58,-38,-40,]),'FN':([0,3,24,29,33,34,35,36,37,39,44,45,49,51,56,58,73,74,75,79,80,81,82,87,89,90,95,96,97,98,99,100,101,102,103,104,105,106,107,113,114,116,119,120,124,125,126,129,131,132,134,135,],[4,4,4,4,-7,-8,-9,-10,-11,-13,-59,-60,4,4,-30,-4,-5,-6,-12,-56,-54,-55,-53,-16,-31,-57,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-39,-20,-58,-38,4,4,-40,-21,-17,4,-19,-22,4,-18,]),'ID':([4,7,20,24,29,33,34,35,36,37,39,40,41,42,43,49,50,51,53,54,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,83,84,85,108,113,115,117,119,120,121,122,125,126,129,130,131,132,134,135,],[6,8,8,26,26,-7,-8,-9,-10,-11,-13,79,79,79,79,26,79,26,79,79,-4,79,79,79,79,79,79,79,79,79,79,79,79,79,79,-5,-6,-12,79,79,111,79,-20,79,79,26,26,79,79,-21,-17,26,79,-19,-22,26,-18,]),'LPAREN':([6,26,47,48,79,],[7,54,84,85,54,]),'RPAREN':([7,9,10,13,14,15,16,17,18,20,22,44,45,54,77,78,79,80,81,82,90,91,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,114,116,118,124,133,],[-3,12,-32,-33,-25,-26,-27,-28,-29,-3,-34,-59,-60,-3,-35,-36,-56,-54,-55,-53,-57,114,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-39,-3,120,-58,-38,-37,-40,134,]),'AS':([8,],[11,]),'INT':([11,19,55,],[14,14,14,]),'STRING':([11,19,24,29,33,34,35,36,37,39,40,41,42,43,49,50,51,53,54,55,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,83,84,108,113,115,117,119,120,121,122,125,126,129,130,131,132,134,135,],[15,15,45,45,-7,-8,-9,-10,-11,-13,45,45,45,45,45,45,45,45,45,15,-4,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-5,-6,-12,45,45,45,-20,45,45,45,45,45,45,-21,-17,45,45,-19,-22,45,-18,]),'VECTOR':([11,19,55,],[16,16,16,]),'NULL':([11,19,55,],[17,17,17,]),'BOOLEAN':([11,19,55,],[18,18,18,]),'LESS_THAN':([12,26,30,44,45,78,79,80,81,82,87,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,114,116,123,124,127,128,133,],[19,-56,66,-59,-60,66,-56,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,-39,66,66,-58,-38,66,66,66,66,66,]),'COMMA':([13,14,15,16,17,18,44,45,78,79,80,81,82,90,95,96,97,98,99,100,101,102,103,104,105,106,107,114,116,124,],[20,-25,-26,-27,-28,-29,-59,-60,108,-56,-54,-55,-53,-57,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-39,-58,-38,-40,]),'GREATER_THAN':([14,15,16,17,18,21,25,26,30,44,45,78,79,80,81,82,87,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,114,116,123,124,127,128,133,],[-25,-26,-27,-28,-29,23,52,-56,65,-59,-60,65,-56,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,-39,65,65,-58,-38,65,65,65,65,65,]),'EQ':([14,15,16,17,18,23,26,79,92,111,],[-25,-26,-27,-28,-29,25,53,53,115,121,]),'SEMI_COLON':([14,15,16,17,18,26,30,31,32,38,44,45,56,79,80,81,82,87,89,90,92,95,96,97,98,99,100,101,102,103,104,105,106,107,114,116,123,124,],[-25,-26,-27,-28,-29,-56,58,73,74,75,-59,-60,-30,-56,-54,-55,-53,-16,-31,-57,-23,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-39,-58,-38,-24,-40,]),'LCURLYEBR':([23,],[24,]),'RCURLYEBR':([24,27,28,29,33,34,35,36,37,39,57,58,73,74,75,113,125,126,131,132,135,],[-3,56,-14,-3,-7,-8,-9,-10,-11,-13,-15,-4,-5,-6,-12,-20,-21,-17,-19,-22,-18,]),'LSQUAREBR':([24,26,29,30,33,34,35,36,37,39,40,41,42,43,44,45,49,50,51,53,54,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,78,79,80,81,82,83,84,87,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,],[40,-56,40,59,-7,-8,-9,-10,-11,-13,40,40,40,40,-59,-60,40,40,40,40,40,-4,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-5,-6,-12,59,-56,59,59,59,40,40,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,-39,40,59,59,-20,-58,40,-38,40,40,40,40,40,59,59,-21,-17,59,59,40,40,-19,-22,59,40,-18,]),'NOT':([24,29,33,34,35,36,37,39,40,41,42,43,49,50,51,53,54,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,83,84,108,113,115,117,119,120,121,122,125,126,129,130,131,132,134,135,],[43,43,-7,-8,-9,-10,-11,-13,43,43,43,43,43,43,43,43,43,-4,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-5,-6,-12,43,43,43,-20,43,43,43,43,43,43,-21,-17,43,43,-19,-22,43,-18,]),'PLUS':([24,26,29,30,33,34,35,36,37,39,40,41,42,43,44,45,49,50,51,53,54,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,78,79,80,81,82,83,84,87,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,],[41,-56,41,61,-7,-8,-9,-10,-11,-13,41,41,41,41,-59,-60,41,41,41,41,41,-4,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-5,-6,-12,61,-56,61,61,61,41,41,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,-39,41,61,61,-20,-58,41,-38,41,41,41,41,41,61,61,-21,-17,61,61,41,41,-19,-22,61,41,-18,]),'MINUS':([24,26,29,30,33,34,35,36,37,39,40,41,42,43,44,45,49,50,51,53,54,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,78,79,80,81,82,83,84,87,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,],[42,-56,42,62,-7,-8,-9,-10,-11,-13,42,42,42,42,-59,-60,42,42,42,42,42,-4,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-5,-6,-12,62,-56,62,62,62,42,42,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,-39,42,62,62,-20,-58,42,-38,42,42,42,42,42,62,62,-21,-17,62,62,42,42,-19,-22,62,42,-18,]),'NUMBER':([24,29,33,34,35,36,37,39,40,41,42,43,49,50,51,53,54,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,83,84,108,113,115,117,119,120,121,122,125,126,129,130,131,132,134,135,],[44,44,-7,-8,-9,-10,-11,-13,44,44,44,44,44,44,44,44,44,-4,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-5,-6,-12,44,44,44,-20,44,44,44,44,44,44,-21,-17,44,44,-19,-22,44,-18,]),'IF':([24,29,33,34,35,36,37,39,49,51,58,73,74,75,113,119,120,125,126,129,131,132,134,135,],[46,46,-7,-8,-9,-10,-11,-13,46,46,-4,-5,-6,-12,-20,46,46,-21,-17,46,-19,-22,46,-18,]),'WHILE':([24,29,33,34,35,36,37,39,49,51,58,73,74,75,86,113,119,120,125,126,129,131,132,134,135,],[47,47,-7,-8,-9,-10,-11,-13,47,47,-4,-5,-6,-12,112,-20,47,47,-21,-17,47,-19,-22,47,-18,]),'FOR':([24,29,33,34,35,36,37,39,49,51,58,73,74,75,113,119,120,125,126,129,131,132,134,135,],[48,48,-7,-8,-9,-10,-11,-13,48,48,-4,-5,-6,-12,-20,48,48,-21,-17,48,-19,-22,48,-18,]),'DO':([24,29,33,34,35,36,37,39,49,51,58,73,74,75,113,119,120,125,126,129,131,132,134,135,],[49,49,-7,-8,-9,-10,-11,-13,49,49,-4,-5,-6,-12,-20,49,49,-21,-17,49,-19,-22,49,-18,]),'RETURN':([24,29,33,34,35,36,37,39,49,51,52,58,73,74,75,113,119,120,125,126,129,131,132,134,135,],[50,50,-7,-8,-9,-10,-11,-13,50,50,50,-4,-5,-6,-12,-20,50,50,-21,-17,50,-19,-22,50,-18,]),'BEGIN':([24,29,33,34,35,36,37,39,49,51,58,73,74,75,113,119,120,125,126,129,131,132,134,135,],[51,51,-7,-8,-9,-10,-11,-13,51,51,-4,-5,-6,-12,-20,51,51,-21,-17,51,-19,-22,51,-18,]),'QUESTION_MARK':([26,30,44,45,78,79,80,81,82,87,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,114,116,123,124,127,128,133,],[-56,60,-59,-60,60,-56,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,-39,60,60,-58,-38,60,60,60,60,60,]),'TIMES':([26,30,44,45,78,79,80,81,82,87,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,114,116,123,124,127,128,133,],[-56,63,-59,-60,63,-56,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,-39,63,63,-58,-38,63,63,63,63,63,]),'DIVIDE':([26,30,44,45,78,79,80,81,82,87,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,114,116,123,124,127,128,133,],[-56,64,-59,-60,64,-56,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,-39,64,64,-58,-38,64,64,64,64,64,]),'DOUBLE_EQ':([26,30,44,45,78,79,80,81,82,87,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,114,116,123,124,127,128,133,],[-56,67,-59,-60,67,-56,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,-39,67,67,-58,-38,67,67,67,67,67,]),'GREATER_THAN_EQ':([26,30,44,45,78,79,80,81,82,87,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,114,116,123,124,127,128,133,],[-56,68,-59,-60,68,-56,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,-39,68,68,-58,-38,68,68,68,68,68,]),'LESS_THAN_EQ':([26,30,44,45,78,79,80,81,82,87,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,114,116,123,124,127,128,133,],[-56,69,-59,-60,69,-56,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,-39,69,69,-58,-38,69,69,69,69,69,]),'NOT_EQ':([26,30,44,45,78,79,80,81,82,87,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,114,116,123,124,127,128,133,],[-56,70,-59,-60,70,-56,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,-39,70,70,-58,-38,70,70,70,70,70,]),'AND':([26,30,44,45,78,79,80,81,82,87,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,114,116,123,124,127,128,133,],[-56,71,-59,-60,71,-56,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,-39,71,71,-58,-38,71,71,71,71,71,]),'OR':([26,30,44,45,78,79,80,81,82,87,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,114,116,123,124,127,128,133,],[-56,72,-59,-60,72,-56,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,-39,72,72,-58,-38,72,72,72,72,72,]),'DBL_COLON':([26,],[55,]),'END':([28,29,33,34,35,36,37,39,51,57,58,73,74,75,88,113,125,126,131,132,135,],[-14,-3,-7,-8,-9,-10,-11,-13,-3,-15,-4,-5,-6,-12,113,-20,-21,-17,-19,-22,-18,]),'ELSE':([33,34,35,36,37,39,58,73,74,75,113,125,126,131,132,135,],[-7,-8,-9,-10,-11,-13,-4,-5,-6,-12,-20,129,-17,-19,-22,-18,]),'RSQUAREBR':([40,44,45,76,77,78,79,80,81,82,90,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,114,116,118,124,],[-3,-59,-60,107,-35,-36,-56,-54,-55,-53,-57,116,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-39,-3,-58,-38,-37,-40,]),'COLON':([44,45,79,80,81,82,90,94,95,96,97,98,99,100,101,102,103,104,105,106,107,114,116,124,],[-59,-60,-56,-54,-55,-53,-57,117,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-39,-58,-38,-40,]),'DOUBLE_RSQUAREBR':([44,45,79,80,81,82,90,95,96,97,98,99,100,101,102,103,104,105,106,107,109,114,116,124,128,],[-59,-60,-56,-54,-55,-53,-57,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-39,119,-58,-38,-40,131,]),'TO':([44,45,79,80,81,82,90,95,96,97,98,99,100,101,102,103,104,105,106,107,114,116,124,127,],[-59,-60,-56,-54,-55,-53,-57,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-39,-58,-38,-40,130,]),'DOUBLE_LSQUAREBR':([46,112,],[83,122,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,3,],[1,5,]),'empty':([0,3,7,20,24,29,40,51,54,108,],[2,2,10,10,28,28,77,28,77,77,]),'func':([0,3,24,29,49,51,119,120,129,134,],[3,3,32,32,32,32,32,32,32,32,]),'flist':([7,20,],[9,22,]),'type':([11,19,55,],[13,21,92,]),'body':([24,29,51,],[27,57,88,]),'stmt':([24,29,49,51,119,120,129,134,],[29,29,86,29,125,126,132,135,]),'expr':([24,29,40,41,42,43,49,50,51,53,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,83,84,108,115,117,119,120,121,122,129,130,134,],[30,30,78,80,81,82,30,87,30,90,78,93,94,95,96,97,98,99,100,101,102,103,104,105,106,109,110,78,123,124,30,30,127,128,30,133,30,]),'defvar':([24,29,49,51,119,120,129,134,],[31,31,31,31,31,31,31,31,]),'single_if':([24,29,49,51,119,120,129,134,],[33,33,33,33,33,33,33,33,]),'else_if':([24,29,49,51,119,120,129,134,],[34,34,34,34,34,34,34,34,]),'while_loop':([24,29,49,51,119,120,129,134,],[35,35,35,35,35,35,35,35,]),'for_loop':([24,29,49,51,119,120,129,134,],[36,36,36,36,36,36,36,36,]),'do_while':([24,29,49,51,119,120,129,134,],[37,37,37,37,37,37,37,37,]),'return_is':([24,29,49,51,52,119,120,129,134,],[38,38,38,38,89,38,38,38,38,]),'block':([24,29,49,51,119,120,129,134,],[39,39,39,39,39,39,39,39,]),'clist':([40,54,108,],[76,91,118,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> empty','prog',1,'p_prog','grammar.py',18),
  ('prog -> func prog','prog',2,'p_prog','grammar.py',19),
  ('empty -> <empty>','empty',0,'p_empty','grammar.py',25),
  ('stmt -> expr SEMI_COLON','stmt',2,'p_stmt','grammar.py',30),
  ('stmt -> defvar SEMI_COLON','stmt',2,'p_stmt','grammar.py',31),
  ('stmt -> func SEMI_COLON','stmt',2,'p_stmt','grammar.py',32),
  ('stmt -> single_if','stmt',1,'p_stmt','grammar.py',33),
  ('stmt -> else_if','stmt',1,'p_stmt','grammar.py',34),
  ('stmt -> while_loop','stmt',1,'p_stmt','grammar.py',35),
  ('stmt -> for_loop','stmt',1,'p_stmt','grammar.py',36),
  ('stmt -> do_while','stmt',1,'p_stmt','grammar.py',37),
  ('stmt -> return_is SEMI_COLON','stmt',2,'p_stmt','grammar.py',38),
  ('stmt -> block','stmt',1,'p_stmt','grammar.py',39),
  ('body -> empty','body',1,'p_body','grammar.py',46),
  ('body -> stmt body','body',2,'p_body','grammar.py',47),
  ('return_is -> RETURN expr','return_is',2,'p_return_is','grammar.py',53),
  ('while_loop -> WHILE LPAREN expr RPAREN stmt','while_loop',5,'p_while_loop','grammar.py',57),
  ('for_loop -> FOR LPAREN ID EQ expr TO expr RPAREN stmt','for_loop',9,'p_for_loop','grammar.py',62),
  ('do_while -> DO stmt WHILE DOUBLE_LSQUAREBR expr DOUBLE_RSQUAREBR','do_while',6,'p_do_while','grammar.py',68),
  ('block -> BEGIN body END','block',3,'p_block','grammar.py',73),
  ('single_if -> IF DOUBLE_LSQUAREBR expr DOUBLE_RSQUAREBR stmt','single_if',5,'p_single_if','grammar.py',77),
  ('else_if -> IF DOUBLE_LSQUAREBR expr DOUBLE_RSQUAREBR stmt ELSE stmt','else_if',7,'p_else_if','grammar.py',81),
  ('defvar -> ID DBL_COLON type','defvar',3,'p_defvar','grammar.py',86),
  ('defvar -> ID DBL_COLON type EQ expr','defvar',5,'p_defvar','grammar.py',87),
  ('type -> INT','type',1,'p_type','grammar.py',95),
  ('type -> STRING','type',1,'p_type','grammar.py',96),
  ('type -> VECTOR','type',1,'p_type','grammar.py',97),
  ('type -> NULL','type',1,'p_type','grammar.py',98),
  ('type -> BOOLEAN','type',1,'p_type','grammar.py',99),
  ('func -> FN ID LPAREN flist RPAREN LESS_THAN type GREATER_THAN LCURLYEBR body RCURLYEBR','func',11,'p_func','grammar.py',104),
  ('func -> FN ID LPAREN flist RPAREN LESS_THAN type GREATER_THAN EQ GREATER_THAN return_is','func',11,'p_func','grammar.py',105),
  ('flist -> empty','flist',1,'p_flist','grammar.py',109),
  ('flist -> ID AS type','flist',3,'p_flist','grammar.py',110),
  ('flist -> ID AS type COMMA flist','flist',5,'p_flist','grammar.py',111),
  ('clist -> empty','clist',1,'p_clist','grammar.py',119),
  ('clist -> expr','clist',1,'p_clist','grammar.py',120),
  ('clist -> expr COMMA clist','clist',3,'p_clist','grammar.py',121),
  ('expr -> expr LSQUAREBR expr RSQUAREBR','expr',4,'p_expr','grammar.py',133),
  ('expr -> LSQUAREBR clist RSQUAREBR','expr',3,'p_expr','grammar.py',134),
  ('expr -> expr QUESTION_MARK expr COLON expr','expr',5,'p_expr','grammar.py',135),
  ('expr -> expr PLUS expr','expr',3,'p_expr','grammar.py',136),
  ('expr -> expr MINUS expr','expr',3,'p_expr','grammar.py',137),
  ('expr -> expr TIMES expr','expr',3,'p_expr','grammar.py',138),
  ('expr -> expr DIVIDE expr','expr',3,'p_expr','grammar.py',139),
  ('expr -> expr GREATER_THAN expr','expr',3,'p_expr','grammar.py',140),
  ('expr -> expr LESS_THAN expr','expr',3,'p_expr','grammar.py',141),
  ('expr -> expr DOUBLE_EQ expr','expr',3,'p_expr','grammar.py',142),
  ('expr -> expr GREATER_THAN_EQ expr','expr',3,'p_expr','grammar.py',143),
  ('expr -> expr LESS_THAN_EQ expr','expr',3,'p_expr','grammar.py',144),
  ('expr -> expr NOT_EQ expr','expr',3,'p_expr','grammar.py',145),
  ('expr -> expr AND expr','expr',3,'p_expr','grammar.py',146),
  ('expr -> expr OR expr','expr',3,'p_expr','grammar.py',147),
  ('expr -> NOT expr','expr',2,'p_expr','grammar.py',148),
  ('expr -> PLUS expr','expr',2,'p_expr','grammar.py',149),
  ('expr -> MINUS expr','expr',2,'p_expr','grammar.py',150),
  ('expr -> ID','expr',1,'p_expr','grammar.py',151),
  ('expr -> ID EQ expr','expr',3,'p_expr','grammar.py',152),
  ('expr -> ID LPAREN clist RPAREN','expr',4,'p_expr','grammar.py',153),
  ('expr -> NUMBER','expr',1,'p_expr','grammar.py',154),
  ('expr -> STRING','expr',1,'p_expr','grammar.py',155),
]
