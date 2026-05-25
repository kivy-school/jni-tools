from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaDescription"]

class MediaDescription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaDescription"
    BT_FOLDER_TYPE_ALBUMS = JavaStaticField("J")
    BT_FOLDER_TYPE_ARTISTS = JavaStaticField("J")
    BT_FOLDER_TYPE_GENRES = JavaStaticField("J")
    BT_FOLDER_TYPE_MIXED = JavaStaticField("J")
    BT_FOLDER_TYPE_PLAYLISTS = JavaStaticField("J")
    BT_FOLDER_TYPE_TITLES = JavaStaticField("J")
    BT_FOLDER_TYPE_YEARS = JavaStaticField("J")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EXTRA_BT_FOLDER_TYPE = JavaStaticField("Ljava/lang/String;")
    getMediaId = JavaMethod("()Ljava/lang/String;")
    getTitle = JavaMethod("()Ljava/lang/CharSequence;")
    getSubtitle = JavaMethod("()Ljava/lang/CharSequence;")
    getDescription = JavaMethod("()Ljava/lang/CharSequence;")
    getIconBitmap = JavaMethod("()Landroid/graphics/Bitmap;")
    getIconUri = JavaMethod("()Landroid/net/Uri;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    getMediaUri = JavaMethod("()Landroid/net/Uri;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaDescription/Builder"
        __javaconstructor__ = [("()V", False)]
        setMediaId = JavaMethod("(Ljava/lang/String;)Landroid/media/MediaDescription$Builder;")
        setTitle = JavaMethod("(Ljava/lang/CharSequence;)Landroid/media/MediaDescription$Builder;")
        setSubtitle = JavaMethod("(Ljava/lang/CharSequence;)Landroid/media/MediaDescription$Builder;")
        setDescription = JavaMethod("(Ljava/lang/CharSequence;)Landroid/media/MediaDescription$Builder;")
        setIconBitmap = JavaMethod("(Landroid/graphics/Bitmap;)Landroid/media/MediaDescription$Builder;")
        setIconUri = JavaMethod("(Landroid/net/Uri;)Landroid/media/MediaDescription$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/media/MediaDescription$Builder;")
        setMediaUri = JavaMethod("(Landroid/net/Uri;)Landroid/media/MediaDescription$Builder;")
        build = JavaMethod("()Landroid/media/MediaDescription;")