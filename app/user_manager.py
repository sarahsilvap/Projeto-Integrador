from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields): 

        #Se faltar algum campo (if None), gera um erro
        if None in (email, password):
            raise ValueError("O campo email e senha são obrigatórios") #raise = "jogar" um erro, igual ao throw em outras linguagens
        
        #Verifica se o e-mail segue um formato de email, como: teste@teste.com. É uma classe existente
        email_ok = self.normalize_email(email)
        
        extra_fields.setdefault("is_active", True)

        #Prepara para salvar no banco. Construção do objeto
        user = self.model(email = email_ok, **extra_fields)

        #Criptografia de senha
        user.set_password(password)

        #Salvar no banco de dados
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        #Poderá acessar a tela de admin do Django
        extra_fields.setdefault("is_staff", True)
        #Seta no bando do Django a propriedade Super User para este usuário
        extra_fields.setdefault("is_superuser", True)

        #chama o método padrão de criação de usuário
        return self.create_user(email, password, **extra_fields)