from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RouteListingPreference"]

class RouteListingPreference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/RouteListingPreference"
    ACTION_TRANSFER_MEDIA = JavaStaticField("Ljava/lang/String;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EXTRA_ROUTE_ID = JavaStaticField("Ljava/lang/String;")
    getItems = JavaMethod("()Ljava/util/List;")
    getUseSystemOrdering = JavaMethod("()Z")
    getLinkedItemComponentName = JavaMethod("()Landroid/content/ComponentName;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/RouteListingPreference/Builder"
        __javaconstructor__ = [("()V", False)]
        setItems = JavaMethod("(Ljava/util/List;)Landroid/media/RouteListingPreference$Builder;")
        setUseSystemOrdering = JavaMethod("(Z)Landroid/media/RouteListingPreference$Builder;")
        setLinkedItemComponentName = JavaMethod("(Landroid/content/ComponentName;)Landroid/media/RouteListingPreference$Builder;")
        build = JavaMethod("()Landroid/media/RouteListingPreference;")

    class Item(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/RouteListingPreference/Item"
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
        getRouteId = JavaMethod("()Ljava/lang/String;")
        getSelectionBehavior = JavaMethod("()I")
        getFlags = JavaMethod("()I")
        getSubText = JavaMethod("()I")
        getCustomSubtextMessage = JavaMethod("()Ljava/lang/CharSequence;")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/media/RouteListingPreference/Item/Builder"
            __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
            setSelectionBehavior = JavaMethod("(I)Landroid/media/RouteListingPreference$Item$Builder;")
            setFlags = JavaMethod("(I)Landroid/media/RouteListingPreference$Item$Builder;")
            setSubText = JavaMethod("(I)Landroid/media/RouteListingPreference$Item$Builder;")
            setCustomSubtextMessage = JavaMethod("(Ljava/lang/CharSequence;)Landroid/media/RouteListingPreference$Item$Builder;")
            build = JavaMethod("()Landroid/media/RouteListingPreference$Item;")