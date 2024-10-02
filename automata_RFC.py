class AFDValidorRFC:
    def __init__(self):
    

        self.states = {
            'q0': self.q0,
            'q1': self.q1,
            'q2': self.q2,
            'q3': self.q3,
            'q4': self.q4,
            'q5': self.q5,
            'q6': self.q6,
            'q7': self.q7,
            'q8': self.q8,
            'q9': self.q9,
            'q10': self.q10,
            'q11': self.q11,
            'q12': self.q12,
            'q13': self.q13,
            'q14': self.q14,
            'q15': self.q15,
            'q16': self.q16,
            'q17': self.q17,
            'q18': self.q18,
            'q19': self.q19,
            'q20': self.q20,
            'q21': self.q21,
            'q22': self.q22,
            'q23': self.q23,
            'q24': self.q24,
            'q25': self.q25,

        }

        self.estado_actual = 'q0'
        self.rfc_actual = ""
        self.rfc_validos = []

    def procesar(self, texto):
        lista_rfc_encontrados = []

        for letra in texto:
            # Usamos la función correspondiente al estado actual
            funcion_estado = self.states[self.estado_actual]
            nuevo_estado = funcion_estado(letra)

            if nuevo_estado:  # Si la transición es válida
                self.rfc_actual += letra  # Añadir el carácter al RFC actual
                self.estado_actual = nuevo_estado
            else:
                # Si llegamos a un estado no válido, reiniciamos
                self.estado_actual = 'q0'
                self.rfc_actual = ""

            # Si llegamos al estado final 'q25'
            if self.estado_actual == 'q25':
                lista_rfc_encontrados.append(self.rfc_actual)
                self.rfc_actual = ""
                self.estado_actual = 'q0'  

        return lista_rfc_encontrados

    def reset(self):
        self.rfc_validos.clear() 
        self.state = 'q0' 
      
    
    def is_letter(self, char):
     return 'A' <= char <= 'Z'


    def is_number(self, char):
     return '0' <= char <= '9'


    def is_number_special_exclude_2(self, char): 
     return char == '1' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9'

    def is_number_special(self, char):
     return char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9'

    def q0(self, char):
     if self.is_letter(char):
       return 'q1'
     return False
    
    def q1(self, char):
     if self.is_letter(char):
       return 'q2'
     return False
    
    def q2(self, char): 
      if self.is_letter(char):
        return 'q3'
      return False
    
    def q3(self, char):
      if self.is_letter(char):
        return 'q4'
      elif self.is_number(char):
        return 'q5'
      else:
        return False
    
    def q4(self, char):
      if self.is_number(char):
        return 'q5'
      return False
    
    def q5(self, char):
      if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
        return 'q6'
      elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
        return 'q7'
      else:
        return False
      
    def q6(self, char):
      if char == '1':
        return 'q9'
      elif char == '0':
        return 'q8'
      else:
        return False
    
    def q7(self, char):
      if char == '1':
        return 'q9'
      elif char == '0':
        return 'q19'
      else:
        return False
      
    def q8(self, char):
      if char == '2':
        return 'q13'
      elif char == '4' or char == '6' or char == '9':
        return 'q11'
      elif char == '1' or char == '3' or char == '5' or char == '7' or char == '8':
        return 'q12'
      else: 
        return False
      
    def q9(self, char): 
      if char == '1':
        return 'q11'
      elif char == '0' or char == '2':
        return 'q10'
      else:
        return False
     
    def q10(self, char):
      if char == '0':
        return 'q17'
      elif char == '1' or char == '2':
        return 'q16'
      elif char == '3':
        return 'q15'
      else:
        return False
    
    def q11(self, char):
      if char == '0':
        return 'q17'
      elif char == '1' or char == '2':
        return 'q16'
      elif char == '3':
        return 'q18'
      else:
        return False
      
    def q12(self, char):
      if char == '0':
        return 'q17'
      elif char == '1' or char == '2':
        return 'q16'
      elif char == '3':
        return 'q15'
      else:
        return False

    def q13(self, char):
      if char == '1' or char == '2':
        return 'q14'
      elif char == '0':
        return 'q17'
      else:
       return False
    
    def q14(self, char):
      if self.is_number(char):
        return 'q22'
      return False
    
    def q15(self, char):
      if char == '0' or char == '1':
        return 'q22'
      return False
    
    def q16(self, char):
      if self.is_number(char):
        return 'q22'
      return False
    
    def q17(self, char):
      if self.is_number_special(char):
        return 'q22'
      return False
    
    def q18(self, char): 
      if char == '0':
        return 'q22'
      return False
    
    def q19(self, char):
      if char == '1' or char == '3' or char == '5' or char == '7' or char == '8':
        return 'q12'
      elif char == '4' or char == '6' or char == '9':
        return 'q11'
      elif char == '2':
        return 'q20'
      else:
        return False
      
    def q20(self, char):
      if char == '2':
        return 'q21'
      elif char == '0':
        return 'q17'
      elif char == '1':
        return 'q14'
      else:
        return False
    
    def q21(self, char):
      if char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8':
        return 'q22'
      return False
    
    def q22(self, char):
      if self.is_letter(char) or self.is_number(char):
        return 'q23'
      return False
    
    def q23(self, char):
      if self.is_letter(char) or self.is_number(char):
        return 'q24'
      return False
    
    def q24(self, char):
      if self.is_letter(char) or self.is_number(char):
        return 'q25'
      return False
    
    def q25(self, char):
      return True
