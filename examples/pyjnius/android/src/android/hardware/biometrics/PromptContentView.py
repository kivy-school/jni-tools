from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PromptContentView"]

class PromptContentView(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/biometrics/PromptContentView"