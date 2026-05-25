from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FormattableFlags"]

class FormattableFlags(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/FormattableFlags"
    ALTERNATE = JavaStaticField("I")
    LEFT_JUSTIFY = JavaStaticField("I")
    UPPERCASE = JavaStaticField("I")