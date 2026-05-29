from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RouteListingPreference"]

class RouteListingPreference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/RouteListingPreference"
    ACTION_TRANSFER_MEDIA = JavaStaticField("Ljava/lang/String;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EXTRA_ROUTE_ID = JavaStaticField("Ljava/lang/String;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getItems = JavaMethod("()Ljava/util/List;")
    getLinkedItemComponentName = JavaMethod("()Landroid/content/ComponentName;")
    getUseSystemOrdering = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Item(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/RouteListingPreference$Item"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        FLAG_ONGOING_SESSION = JavaStaticField("I")
        FLAG_ONGOING_SESSION_MANAGED = JavaStaticField("I")
        FLAG_SUGGESTED = JavaStaticField("I")
        SELECTION_BEHAVIOR_GO_TO_APP = JavaStaticField("I")
        SELECTION_BEHAVIOR_NONE = JavaStaticField("I")
        SELECTION_BEHAVIOR_TRANSFER = JavaStaticField("I")
        SUBTEXT_AD_ROUTING_DISALLOWED = JavaStaticField("I")
        SUBTEXT_CUSTOM = JavaStaticField("I")
        SUBTEXT_DEVICE_LOW_POWER = JavaStaticField("I")
        SUBTEXT_DOWNLOADED_CONTENT_ROUTING_DISALLOWED = JavaStaticField("I")
        SUBTEXT_ERROR_UNKNOWN = JavaStaticField("I")
        SUBTEXT_NONE = JavaStaticField("I")
        SUBTEXT_SUBSCRIPTION_REQUIRED = JavaStaticField("I")
        SUBTEXT_TRACK_UNSUPPORTED = JavaStaticField("I")
        SUBTEXT_UNAUTHORIZED = JavaStaticField("I")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        getRouteId = JavaMethod("()Ljava/lang/String;")
        getSubText = JavaMethod("()I")
        getCustomSubtextMessage = JavaMethod("()Ljava/lang/CharSequence;")
        getSelectionBehavior = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getFlags = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/media/RouteListingPreference$Item$Builder"
            __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
            setSelectionBehavior = JavaMethod("(I)Landroid/media/RouteListingPreference$Item$Builder;")
            setCustomSubtextMessage = JavaMethod("(Ljava/lang/CharSequence;)Landroid/media/RouteListingPreference$Item$Builder;")
            setFlags = JavaMethod("(I)Landroid/media/RouteListingPreference$Item$Builder;")
            build = JavaMethod("()Landroid/media/RouteListingPreference$Item;")
            setSubText = JavaMethod("(I)Landroid/media/RouteListingPreference$Item$Builder;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/RouteListingPreference$Builder"
        __javaconstructor__ = [("()V", False)]
        setLinkedItemComponentName = JavaMethod("(Landroid/content/ComponentName;)Landroid/media/RouteListingPreference$Builder;")
        setUseSystemOrdering = JavaMethod("(Z)Landroid/media/RouteListingPreference$Builder;")
        build = JavaMethod("()Landroid/media/RouteListingPreference;")
        setItems = JavaMethod("(Ljava/util/List;)Landroid/media/RouteListingPreference$Builder;")