from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JsonToken"]

class JsonToken(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/JsonToken"
    BEGIN_ARRAY = JavaStaticField("Landroid/util/JsonToken;")
    BEGIN_OBJECT = JavaStaticField("Landroid/util/JsonToken;")
    BOOLEAN = JavaStaticField("Landroid/util/JsonToken;")
    END_ARRAY = JavaStaticField("Landroid/util/JsonToken;")
    END_DOCUMENT = JavaStaticField("Landroid/util/JsonToken;")
    END_OBJECT = JavaStaticField("Landroid/util/JsonToken;")
    NAME = JavaStaticField("Landroid/util/JsonToken;")
    NULL = JavaStaticField("Landroid/util/JsonToken;")
    NUMBER = JavaStaticField("Landroid/util/JsonToken;")
    STRING = JavaStaticField("Landroid/util/JsonToken;")
    values = JavaStaticMethod("()[Landroid/util/JsonToken;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/util/JsonToken;")
    BEGIN_ARRAY = JavaStaticField("Landroid/util/JsonToken;")
    BEGIN_OBJECT = JavaStaticField("Landroid/util/JsonToken;")
    BOOLEAN = JavaStaticField("Landroid/util/JsonToken;")
    END_ARRAY = JavaStaticField("Landroid/util/JsonToken;")
    END_DOCUMENT = JavaStaticField("Landroid/util/JsonToken;")
    END_OBJECT = JavaStaticField("Landroid/util/JsonToken;")
    NAME = JavaStaticField("Landroid/util/JsonToken;")
    NULL = JavaStaticField("Landroid/util/JsonToken;")
    NUMBER = JavaStaticField("Landroid/util/JsonToken;")
    STRING = JavaStaticField("Landroid/util/JsonToken;")