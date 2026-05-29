from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Entity"]

class Entity(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/Entity"
    __javaconstructor__ = [("(Landroid/content/ContentValues;)V", False)]
    getEntityValues = JavaMethod("()Landroid/content/ContentValues;")
    getSubValues = JavaMethod("()Ljava/util/ArrayList;")
    addSubValue = JavaMethod("(Landroid/net/Uri;Landroid/content/ContentValues;)V")
    toString = JavaMethod("()Ljava/lang/String;")

    class NamedContentValues(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/Entity/NamedContentValues"
        __javaconstructor__ = [("(Landroid/net/Uri;Landroid/content/ContentValues;)V", False)]
        uri = JavaField("Landroid/net/Uri;")
        values = JavaField("Landroid/content/ContentValues;")