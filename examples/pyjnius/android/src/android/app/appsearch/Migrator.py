from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Migrator"]

class Migrator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/Migrator"
    __javaconstructor__ = [("()V", False)]
    shouldMigrate = JavaMethod("(II)Z")
    onUpgrade = JavaMethod("(IILandroid/app/appsearch/GenericDocument;)Landroid/app/appsearch/GenericDocument;")
    onDowngrade = JavaMethod("(IILandroid/app/appsearch/GenericDocument;)Landroid/app/appsearch/GenericDocument;")