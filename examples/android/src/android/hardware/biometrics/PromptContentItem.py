from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PromptContentItem"]

class PromptContentItem(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/biometrics/PromptContentItem"