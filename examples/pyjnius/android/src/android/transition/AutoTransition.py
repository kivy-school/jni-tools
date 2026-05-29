from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AutoTransition"]

class AutoTransition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/AutoTransition"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    ORDERING_SEQUENTIAL = JavaStaticField("I")
    ORDERING_TOGETHER = JavaStaticField("I")
    MATCH_ID = JavaStaticField("I")
    MATCH_INSTANCE = JavaStaticField("I")
    MATCH_ITEM_ID = JavaStaticField("I")
    MATCH_NAME = JavaStaticField("I")