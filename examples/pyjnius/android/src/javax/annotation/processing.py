from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class Generated(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/annotation/processing/Generated"
    value = JavaMethod("()[Ljava/lang/String;")
    comments = JavaMethod("()Ljava/lang/String;")
    date = JavaMethod("()Ljava/lang/String;")