from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SliceManager"]

class SliceManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/slice/SliceManager"
    CATEGORY_SLICE = JavaStaticField("Ljava/lang/String;")
    SLICE_METADATA_KEY = JavaStaticField("Ljava/lang/String;")
    pinSlice = JavaMethod("(Landroid/net/Uri;Ljava/util/Set;)V")
    unpinSlice = JavaMethod("(Landroid/net/Uri;)V")
    getPinnedSpecs = JavaMethod("(Landroid/net/Uri;)Ljava/util/Set;")
    getPinnedSlices = JavaMethod("()Ljava/util/List;")
    getSliceDescendants = JavaMethod("(Landroid/net/Uri;)Ljava/util/Collection;")
    bindSlice = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/util/Set;)Landroid/app/slice/Slice;", False, False), ("(Landroid/content/Intent;Ljava/util/Set;)Landroid/app/slice/Slice;", False, False)])
    mapIntentToUri = JavaMethod("(Landroid/content/Intent;)Landroid/net/Uri;")
    checkSlicePermission = JavaMethod("(Landroid/net/Uri;II)I")
    grantSlicePermission = JavaMethod("(Ljava/lang/String;Landroid/net/Uri;)V")
    revokeSlicePermission = JavaMethod("(Ljava/lang/String;Landroid/net/Uri;)V")