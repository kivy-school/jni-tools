from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DevicePolicyResourcesManager"]

class DevicePolicyResourcesManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/DevicePolicyResourcesManager"
    getDrawable = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;Ljava/util/function/Supplier;)Landroid/graphics/drawable/Drawable;", False, False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/util/function/Supplier;)Landroid/graphics/drawable/Drawable;", False, False)])
    getDrawableForDensity = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;ILjava/util/function/Supplier;)Landroid/graphics/drawable/Drawable;", False, False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;ILjava/util/function/Supplier;)Landroid/graphics/drawable/Drawable;", False, False)])
    getDrawableAsIcon = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/graphics/drawable/Icon;)Landroid/graphics/drawable/Icon;", False, False), ("(Ljava/lang/String;Ljava/lang/String;Landroid/graphics/drawable/Icon;)Landroid/graphics/drawable/Icon;", False, False)])
    getString = JavaMultipleMethod([("(Ljava/lang/String;Ljava/util/function/Supplier;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Ljava/util/function/Supplier;[Ljava/lang/Object;)Ljava/lang/String;", False, True)])