from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class Repeatable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/Repeatable"
    value = JavaMethod("()Ljava/lang/Class;")

class Retention(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/Retention"
    value = JavaMethod("()Ljava/lang/annotation/RetentionPolicy;")

class Target(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/Target"
    value = JavaMethod("()[Ljava/lang/annotation/ElementType;")

class Documented(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/Documented"

class AnnotationFormatError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/AnnotationFormatError"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/Throwable;)V", False)]

class IncompleteAnnotationException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/IncompleteAnnotationException"
    __javaconstructor__ = [("(Ljava/lang/Class;Ljava/lang/String;)V", False)]
    annotationType = JavaMethod("()Ljava/lang/Class;")
    elementName = JavaMethod("()Ljava/lang/String;")

class Native(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/Native"

class Inherited(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/Inherited"

class AnnotationTypeMismatchException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/AnnotationTypeMismatchException"
    __javaconstructor__ = [("(Ljava/lang/reflect/Method;Ljava/lang/String;)V", False)]
    foundType = JavaMethod("()Ljava/lang/String;")
    element = JavaMethod("()Ljava/lang/reflect/Method;")

class RetentionPolicy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/RetentionPolicy"
    SOURCE = JavaStaticField("Ljava/lang/annotation/RetentionPolicy;")
    CLASS = JavaStaticField("Ljava/lang/annotation/RetentionPolicy;")
    RUNTIME = JavaStaticField("Ljava/lang/annotation/RetentionPolicy;")
    values = JavaStaticMethod("()[Ljava/lang/annotation/RetentionPolicy;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/annotation/RetentionPolicy;")
    SOURCE = JavaStaticField("Ljava/lang/annotation/RetentionPolicy;")
    CLASS = JavaStaticField("Ljava/lang/annotation/RetentionPolicy;")
    RUNTIME = JavaStaticField("Ljava/lang/annotation/RetentionPolicy;")

class ElementType(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/ElementType"
    TYPE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    FIELD = JavaStaticField("Ljava/lang/annotation/ElementType;")
    METHOD = JavaStaticField("Ljava/lang/annotation/ElementType;")
    PARAMETER = JavaStaticField("Ljava/lang/annotation/ElementType;")
    CONSTRUCTOR = JavaStaticField("Ljava/lang/annotation/ElementType;")
    LOCAL_VARIABLE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    ANNOTATION_TYPE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    PACKAGE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    TYPE_PARAMETER = JavaStaticField("Ljava/lang/annotation/ElementType;")
    TYPE_USE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    MODULE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    RECORD_COMPONENT = JavaStaticField("Ljava/lang/annotation/ElementType;")
    values = JavaStaticMethod("()[Ljava/lang/annotation/ElementType;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/annotation/ElementType;")
    TYPE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    FIELD = JavaStaticField("Ljava/lang/annotation/ElementType;")
    METHOD = JavaStaticField("Ljava/lang/annotation/ElementType;")
    PARAMETER = JavaStaticField("Ljava/lang/annotation/ElementType;")
    CONSTRUCTOR = JavaStaticField("Ljava/lang/annotation/ElementType;")
    LOCAL_VARIABLE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    ANNOTATION_TYPE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    PACKAGE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    TYPE_PARAMETER = JavaStaticField("Ljava/lang/annotation/ElementType;")
    TYPE_USE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    MODULE = JavaStaticField("Ljava/lang/annotation/ElementType;")
    RECORD_COMPONENT = JavaStaticField("Ljava/lang/annotation/ElementType;")

class Annotation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/Annotation"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    annotationType = JavaMethod("()Ljava/lang/Class;")