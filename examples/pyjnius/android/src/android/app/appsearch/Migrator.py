from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Migrator"]

class Migrator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/Migrator"
    __javaconstructor__ = [("()V", False)]
    onDowngrade = JavaMethod("(IILandroid/app/appsearch/GenericDocument;)Landroid/app/appsearch/GenericDocument;")
    onUpgrade = JavaMethod("(IILandroid/app/appsearch/GenericDocument;)Landroid/app/appsearch/GenericDocument;")
    shouldMigrate = JavaMethod("(II)Z")