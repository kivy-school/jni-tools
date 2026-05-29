from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FormattableFlags"]

class FormattableFlags(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/FormattableFlags"
    LEFT_JUSTIFY = JavaStaticField("I")
    UPPERCASE = JavaStaticField("I")
    ALTERNATE = JavaStaticField("I")