from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThumbnailTemplate"]

class ThumbnailTemplate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/controls/templates/ThumbnailTemplate"
    __javaconstructor__ = [("(Ljava/lang/String;ZLandroid/graphics/drawable/Icon;Ljava/lang/CharSequence;)V", False)]
    TYPE_ERROR = JavaStaticField("I")
    TYPE_NO_TEMPLATE = JavaStaticField("I")
    TYPE_RANGE = JavaStaticField("I")
    TYPE_STATELESS = JavaStaticField("I")
    TYPE_TEMPERATURE = JavaStaticField("I")
    TYPE_THUMBNAIL = JavaStaticField("I")
    TYPE_TOGGLE = JavaStaticField("I")
    TYPE_TOGGLE_RANGE = JavaStaticField("I")
    getTemplateType = JavaMethod("()I")
    getContentDescription = JavaMethod("()Ljava/lang/CharSequence;")
    getThumbnail = JavaMethod("()Landroid/graphics/drawable/Icon;")
    isActive = JavaMethod("()Z")