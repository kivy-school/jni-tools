from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class SuppressLint(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/annotation/SuppressLint"
    value = JavaMethod("()[Ljava/lang/String;")

class TargetApi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/annotation/TargetApi"
    value = JavaMethod("()I")