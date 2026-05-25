from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThumbnailTemplate"]

class ThumbnailTemplate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/controls/templates/ThumbnailTemplate"
    __javaconstructor__ = [("(Ljava/lang/String;ZLandroid/graphics/drawable/Icon;Ljava/lang/CharSequence;)V", False)]
    isActive = JavaMethod("()Z")
    getThumbnail = JavaMethod("()Landroid/graphics/drawable/Icon;")
    getContentDescription = JavaMethod("()Ljava/lang/CharSequence;")
    getTemplateType = JavaMethod("()I")