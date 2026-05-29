from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SliceManager"]

class SliceManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/slice/SliceManager"
    CATEGORY_SLICE = JavaStaticField("Ljava/lang/String;")
    SLICE_METADATA_KEY = JavaStaticField("Ljava/lang/String;")
    bindSlice = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/util/Set;)Landroid/app/slice/Slice;", False, False), ("(Landroid/content/Intent;Ljava/util/Set;)Landroid/app/slice/Slice;", False, False)])
    checkSlicePermission = JavaMethod("(Landroid/net/Uri;II)I")
    getPinnedSlices = JavaMethod("()Ljava/util/List;")
    getPinnedSpecs = JavaMethod("(Landroid/net/Uri;)Ljava/util/Set;")
    getSliceDescendants = JavaMethod("(Landroid/net/Uri;)Ljava/util/Collection;")
    grantSlicePermission = JavaMethod("(Ljava/lang/String;Landroid/net/Uri;)V")
    mapIntentToUri = JavaMethod("(Landroid/content/Intent;)Landroid/net/Uri;")
    pinSlice = JavaMethod("(Landroid/net/Uri;Ljava/util/Set;)V")
    revokeSlicePermission = JavaMethod("(Ljava/lang/String;Landroid/net/Uri;)V")
    unpinSlice = JavaMethod("(Landroid/net/Uri;)V")