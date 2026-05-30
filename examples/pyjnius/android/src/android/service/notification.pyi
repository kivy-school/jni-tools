from typing import Any, ClassVar, overload
from android.app.NotificationChannel import NotificationChannel
from android.app.NotificationChannelGroup import NotificationChannelGroup
from android.content.ComponentName import ComponentName
from android.content.Intent import Intent
from android.content.pm.ShortcutInfo import ShortcutInfo
from android.os.IBinder import IBinder
from android.os.Parcel import Parcel
from android.os.UserHandle import UserHandle
from android.service.notification.StatusBarNotification import StatusBarNotification

class NotificationListenerService:
    ACTION_SETTINGS_HOME: ClassVar[str]
    FLAG_FILTER_TYPE_ALERTING: ClassVar[int]
    FLAG_FILTER_TYPE_CONVERSATIONS: ClassVar[int]
    FLAG_FILTER_TYPE_ONGOING: ClassVar[int]
    FLAG_FILTER_TYPE_SILENT: ClassVar[int]
    HINT_HOST_DISABLE_CALL_EFFECTS: ClassVar[int]
    HINT_HOST_DISABLE_EFFECTS: ClassVar[int]
    HINT_HOST_DISABLE_NOTIFICATION_EFFECTS: ClassVar[int]
    INTERRUPTION_FILTER_ALARMS: ClassVar[int]
    INTERRUPTION_FILTER_ALL: ClassVar[int]
    INTERRUPTION_FILTER_NONE: ClassVar[int]
    INTERRUPTION_FILTER_PRIORITY: ClassVar[int]
    INTERRUPTION_FILTER_UNKNOWN: ClassVar[int]
    META_DATA_DEFAULT_AUTOBIND: ClassVar[str]
    META_DATA_DEFAULT_FILTER_TYPES: ClassVar[str]
    META_DATA_DISABLED_FILTER_TYPES: ClassVar[str]
    NOTIFICATION_CHANNEL_OR_GROUP_ADDED: ClassVar[int]
    NOTIFICATION_CHANNEL_OR_GROUP_DELETED: ClassVar[int]
    NOTIFICATION_CHANNEL_OR_GROUP_UPDATED: ClassVar[int]
    REASON_APP_CANCEL: ClassVar[int]
    REASON_APP_CANCEL_ALL: ClassVar[int]
    REASON_ASSISTANT_CANCEL: ClassVar[int]
    REASON_CANCEL: ClassVar[int]
    REASON_CANCEL_ALL: ClassVar[int]
    REASON_CHANNEL_BANNED: ClassVar[int]
    REASON_CHANNEL_REMOVED: ClassVar[int]
    REASON_CLEAR_DATA: ClassVar[int]
    REASON_CLICK: ClassVar[int]
    REASON_ERROR: ClassVar[int]
    REASON_GROUP_OPTIMIZATION: ClassVar[int]
    REASON_GROUP_SUMMARY_CANCELED: ClassVar[int]
    REASON_LISTENER_CANCEL: ClassVar[int]
    REASON_LISTENER_CANCEL_ALL: ClassVar[int]
    REASON_LOCKDOWN: ClassVar[int]
    REASON_PACKAGE_BANNED: ClassVar[int]
    REASON_PACKAGE_CHANGED: ClassVar[int]
    REASON_PACKAGE_SUSPENDED: ClassVar[int]
    REASON_PROFILE_TURNED_OFF: ClassVar[int]
    REASON_SNOOZED: ClassVar[int]
    REASON_TIMEOUT: ClassVar[int]
    REASON_UNAUTOBUNDLED: ClassVar[int]
    REASON_USER_STOPPED: ClassVar[int]
    SERVICE_INTERFACE: ClassVar[str]
    SUPPRESSED_EFFECT_SCREEN_OFF: ClassVar[int]
    SUPPRESSED_EFFECT_SCREEN_ON: ClassVar[int]
    START_CONTINUATION_MASK: ClassVar[int]
    START_FLAG_REDELIVERY: ClassVar[int]
    START_FLAG_RETRY: ClassVar[int]
    START_NOT_STICKY: ClassVar[int]
    START_REDELIVER_INTENT: ClassVar[int]
    START_STICKY: ClassVar[int]
    START_STICKY_COMPATIBILITY: ClassVar[int]
    STOP_FOREGROUND_DETACH: ClassVar[int]
    STOP_FOREGROUND_LEGACY: ClassVar[int]
    STOP_FOREGROUND_REMOVE: ClassVar[int]
    TRIM_MEMORY_BACKGROUND: ClassVar[int]
    TRIM_MEMORY_COMPLETE: ClassVar[int]
    TRIM_MEMORY_MODERATE: ClassVar[int]
    TRIM_MEMORY_RUNNING_CRITICAL: ClassVar[int]
    TRIM_MEMORY_RUNNING_LOW: ClassVar[int]
    TRIM_MEMORY_RUNNING_MODERATE: ClassVar[int]
    TRIM_MEMORY_UI_HIDDEN: ClassVar[int]
    ACCESSIBILITY_SERVICE: ClassVar[str]
    ACCOUNT_SERVICE: ClassVar[str]
    ACTIVITY_SERVICE: ClassVar[str]
    ADVANCED_PROTECTION_SERVICE: ClassVar[str]
    ALARM_SERVICE: ClassVar[str]
    APPWIDGET_SERVICE: ClassVar[str]
    APP_FUNCTION_SERVICE: ClassVar[str]
    APP_OPS_SERVICE: ClassVar[str]
    APP_SEARCH_SERVICE: ClassVar[str]
    AUDIO_SERVICE: ClassVar[str]
    BATTERY_SERVICE: ClassVar[str]
    BIND_ABOVE_CLIENT: ClassVar[int]
    BIND_ADJUST_WITH_ACTIVITY: ClassVar[int]
    BIND_ALLOW_ACTIVITY_STARTS: ClassVar[int]
    BIND_ALLOW_OOM_MANAGEMENT: ClassVar[int]
    BIND_AUTO_CREATE: ClassVar[int]
    BIND_DEBUG_UNBIND: ClassVar[int]
    BIND_EXTERNAL_SERVICE: ClassVar[int]
    BIND_EXTERNAL_SERVICE_LONG: ClassVar[int]
    BIND_IMPORTANT: ClassVar[int]
    BIND_INCLUDE_CAPABILITIES: ClassVar[int]
    BIND_NOT_FOREGROUND: ClassVar[int]
    BIND_NOT_PERCEPTIBLE: ClassVar[int]
    BIND_PACKAGE_ISOLATED_PROCESS: ClassVar[int]
    BIND_SHARED_ISOLATED_PROCESS: ClassVar[int]
    BIND_WAIVE_PRIORITY: ClassVar[int]
    BIOMETRIC_SERVICE: ClassVar[str]
    BLOB_STORE_SERVICE: ClassVar[str]
    BLUETOOTH_SERVICE: ClassVar[str]
    BUGREPORT_SERVICE: ClassVar[str]
    CAMERA_SERVICE: ClassVar[str]
    CAPTIONING_SERVICE: ClassVar[str]
    CARRIER_CONFIG_SERVICE: ClassVar[str]
    CLIPBOARD_SERVICE: ClassVar[str]
    COMPANION_DEVICE_SERVICE: ClassVar[str]
    CONNECTIVITY_DIAGNOSTICS_SERVICE: ClassVar[str]
    CONNECTIVITY_SERVICE: ClassVar[str]
    CONSUMER_IR_SERVICE: ClassVar[str]
    CONTACT_KEYS_SERVICE: ClassVar[str]
    CONTEXT_IGNORE_SECURITY: ClassVar[int]
    CONTEXT_INCLUDE_CODE: ClassVar[int]
    CONTEXT_RESTRICTED: ClassVar[int]
    CREDENTIAL_SERVICE: ClassVar[str]
    CROSS_PROFILE_APPS_SERVICE: ClassVar[str]
    DEVICE_ID_DEFAULT: ClassVar[int]
    DEVICE_ID_INVALID: ClassVar[int]
    DEVICE_LOCK_SERVICE: ClassVar[str]
    DEVICE_POLICY_SERVICE: ClassVar[str]
    DISPLAY_HASH_SERVICE: ClassVar[str]
    DISPLAY_SERVICE: ClassVar[str]
    DOMAIN_VERIFICATION_SERVICE: ClassVar[str]
    DOWNLOAD_SERVICE: ClassVar[str]
    DROPBOX_SERVICE: ClassVar[str]
    EUICC_SERVICE: ClassVar[str]
    FILE_INTEGRITY_SERVICE: ClassVar[str]
    FINGERPRINT_SERVICE: ClassVar[str]
    GAME_SERVICE: ClassVar[str]
    GRAMMATICAL_INFLECTION_SERVICE: ClassVar[str]
    HARDWARE_PROPERTIES_SERVICE: ClassVar[str]
    HEALTHCONNECT_SERVICE: ClassVar[str]
    INPUT_METHOD_SERVICE: ClassVar[str]
    INPUT_SERVICE: ClassVar[str]
    IPSEC_SERVICE: ClassVar[str]
    JOB_SCHEDULER_SERVICE: ClassVar[str]
    KEYGUARD_SERVICE: ClassVar[str]
    KEYSTORE_SERVICE: ClassVar[str]
    LAUNCHER_APPS_SERVICE: ClassVar[str]
    LAYOUT_INFLATER_SERVICE: ClassVar[str]
    LOCALE_SERVICE: ClassVar[str]
    LOCATION_SERVICE: ClassVar[str]
    MEDIA_COMMUNICATION_SERVICE: ClassVar[str]
    MEDIA_METRICS_SERVICE: ClassVar[str]
    MEDIA_PROJECTION_SERVICE: ClassVar[str]
    MEDIA_QUALITY_SERVICE: ClassVar[str]
    MEDIA_ROUTER_SERVICE: ClassVar[str]
    MEDIA_SESSION_SERVICE: ClassVar[str]
    MIDI_SERVICE: ClassVar[str]
    MODE_APPEND: ClassVar[int]
    MODE_ENABLE_WRITE_AHEAD_LOGGING: ClassVar[int]
    MODE_MULTI_PROCESS: ClassVar[int]
    MODE_NO_LOCALIZED_COLLATORS: ClassVar[int]
    MODE_PRIVATE: ClassVar[int]
    MODE_WORLD_READABLE: ClassVar[int]
    MODE_WORLD_WRITEABLE: ClassVar[int]
    NETWORK_STATS_SERVICE: ClassVar[str]
    NFC_SERVICE: ClassVar[str]
    NOTIFICATION_SERVICE: ClassVar[str]
    NSD_SERVICE: ClassVar[str]
    OVERLAY_SERVICE: ClassVar[str]
    PEOPLE_SERVICE: ClassVar[str]
    PERFORMANCE_HINT_SERVICE: ClassVar[str]
    PERSISTENT_DATA_BLOCK_SERVICE: ClassVar[str]
    POWER_SERVICE: ClassVar[str]
    PRINT_SERVICE: ClassVar[str]
    PROFILING_SERVICE: ClassVar[str]
    RECEIVER_EXPORTED: ClassVar[int]
    RECEIVER_NOT_EXPORTED: ClassVar[int]
    RECEIVER_VISIBLE_TO_INSTANT_APPS: ClassVar[int]
    RESTRICTIONS_SERVICE: ClassVar[str]
    ROLE_SERVICE: ClassVar[str]
    SATELLITE_SERVICE: ClassVar[str]
    SEARCH_SERVICE: ClassVar[str]
    SECURITY_STATE_SERVICE: ClassVar[str]
    SENSOR_SERVICE: ClassVar[str]
    SHORTCUT_SERVICE: ClassVar[str]
    STATUS_BAR_SERVICE: ClassVar[str]
    STORAGE_SERVICE: ClassVar[str]
    STORAGE_STATS_SERVICE: ClassVar[str]
    SYSTEM_HEALTH_SERVICE: ClassVar[str]
    TELECOM_SERVICE: ClassVar[str]
    TELEPHONY_IMS_SERVICE: ClassVar[str]
    TELEPHONY_SERVICE: ClassVar[str]
    TELEPHONY_SUBSCRIPTION_SERVICE: ClassVar[str]
    TETHERING_SERVICE: ClassVar[str]
    TEXT_CLASSIFICATION_SERVICE: ClassVar[str]
    TEXT_SERVICES_MANAGER_SERVICE: ClassVar[str]
    TV_AD_SERVICE: ClassVar[str]
    TV_INPUT_SERVICE: ClassVar[str]
    TV_INTERACTIVE_APP_SERVICE: ClassVar[str]
    UI_MODE_SERVICE: ClassVar[str]
    USAGE_STATS_SERVICE: ClassVar[str]
    USB_SERVICE: ClassVar[str]
    USER_SERVICE: ClassVar[str]
    VIBRATOR_MANAGER_SERVICE: ClassVar[str]
    VIBRATOR_SERVICE: ClassVar[str]
    VIRTUAL_DEVICE_SERVICE: ClassVar[str]
    VPN_MANAGEMENT_SERVICE: ClassVar[str]
    WALLPAPER_SERVICE: ClassVar[str]
    WIFI_AWARE_SERVICE: ClassVar[str]
    WIFI_P2P_SERVICE: ClassVar[str]
    WIFI_RTT_RANGING_SERVICE: ClassVar[str]
    WIFI_SERVICE: ClassVar[str]
    WINDOW_SERVICE: ClassVar[str]
    def __init__(self) -> None: ...
    def cancelAllNotifications(self) -> None: ...
    @overload
    def cancelNotification(self, p0: str, p1: str, p2: int) -> None: ...
    @overload
    def cancelNotification(self, p0: str) -> None: ...
    def cancelNotifications(self, p0: Any) -> None: ...
    def clearRequestedListenerHints(self) -> None: ...
    def createConversationNotificationChannelForPackage(self, p0: str, p1: UserHandle, p2: str, p3: str) -> NotificationChannel: ...
    @overload
    def getActiveNotifications(self, p0: Any) -> Any: ...
    @overload
    def getActiveNotifications(self) -> Any: ...
    def getCurrentInterruptionFilter(self) -> int: ...
    def getCurrentListenerHints(self) -> int: ...
    def getCurrentRanking(self) -> Any: ...
    def getNotificationChannelGroups(self, p0: str, p1: UserHandle) -> list: ...
    def getNotificationChannels(self, p0: str, p1: UserHandle) -> list: ...
    def getSnoozedNotifications(self) -> Any: ...
    def migrateNotificationFilter(self, p0: int, p1: list) -> None: ...
    def onInterruptionFilterChanged(self, p0: int) -> None: ...
    def onListenerConnected(self) -> None: ...
    def onListenerDisconnected(self) -> None: ...
    def onListenerHintsChanged(self, p0: int) -> None: ...
    def onNotificationChannelGroupModified(self, p0: str, p1: UserHandle, p2: NotificationChannelGroup, p3: int) -> None: ...
    def onNotificationChannelModified(self, p0: str, p1: UserHandle, p2: NotificationChannel, p3: int) -> None: ...
    @overload
    def onNotificationPosted(self, p0: StatusBarNotification, p1: Any) -> None: ...
    @overload
    def onNotificationPosted(self, p0: StatusBarNotification) -> None: ...
    def onNotificationRankingUpdate(self, p0: Any) -> None: ...
    @overload
    def onNotificationRemoved(self, p0: StatusBarNotification, p1: Any) -> None: ...
    @overload
    def onNotificationRemoved(self, p0: StatusBarNotification) -> None: ...
    @overload
    def onNotificationRemoved(self, p0: StatusBarNotification, p1: Any, p2: int) -> None: ...
    def onSilentStatusBarIconsVisibilityChanged(self, p0: bool) -> None: ...
    def requestInterruptionFilter(self, p0: int) -> None: ...
    def requestListenerHints(self, p0: int) -> None: ...
    @staticmethod
    def requestRebind(p0: ComponentName) -> None: ...
    @overload
    def requestUnbind(self) -> None: ...
    @overload
    @staticmethod
    def requestUnbind(p0: ComponentName) -> None: ...
    def setNotificationsShown(self, p0: Any) -> None: ...
    def snoozeNotification(self, p0: str, p1: int) -> None: ...
    def updateNotificationChannel(self, p0: str, p1: UserHandle, p2: NotificationChannel) -> None: ...
    def onBind(self, p0: Intent) -> IBinder: ...
    def onDestroy(self) -> None: ...

    class RankingMap:
        CREATOR: ClassVar[Any]
        CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
        PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
        def getOrderedKeys(self) -> Any: ...
        def getRanking(self, p0: str, p1: Any) -> bool: ...
        def equals(self, p0: Any) -> bool: ...
        def describeContents(self) -> int: ...
        def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Ranking:
        USER_SENTIMENT_NEGATIVE: ClassVar[int]
        USER_SENTIMENT_NEUTRAL: ClassVar[int]
        USER_SENTIMENT_POSITIVE: ClassVar[int]
        VISIBILITY_NO_OVERRIDE: ClassVar[int]
        def __init__(self) -> None: ...
        def getRank(self) -> int: ...
        def canBubble(self) -> bool: ...
        def canShowBadge(self) -> bool: ...
        def getImportance(self) -> int: ...
        def isConversation(self) -> bool: ...
        def getOverrideGroupKey(self) -> str: ...
        def getSmartReplies(self) -> list: ...
        def getSuppressedVisualEffects(self) -> int: ...
        def getUserSentiment(self) -> int: ...
        def matchesInterruptionFilter(self) -> bool: ...
        def isSuspended(self) -> bool: ...
        def getConversationShortcutInfo(self) -> ShortcutInfo: ...
        def getImportanceExplanation(self) -> str: ...
        def getLastAudiblyAlertedMillis(self) -> int: ...
        def getLockscreenVisibilityOverride(self) -> int: ...
        def getSmartActions(self) -> list: ...
        def isAmbient(self) -> bool: ...
        def equals(self, p0: Any) -> bool: ...
        def getKey(self) -> str: ...
        def getChannel(self) -> NotificationChannel: ...

from typing import Any, ClassVar, overload
from android.app.Notification import Notification
from android.os.Parcel import Parcel
from android.os.UserHandle import UserHandle

class StatusBarNotification:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @overload
    def __init__(self, p0: str, p1: str, p2: int, p3: str, p4: int, p5: int, p6: int, p7: Notification, p8: UserHandle, p9: int) -> None: ...
    @overload
    def __init__(self, p0: Parcel) -> None: ...
    def getGroupKey(self) -> str: ...
    def getNotification(self) -> Notification: ...
    def getOpPkg(self) -> str: ...
    def getOverrideGroupKey(self) -> str: ...
    def getPostTime(self) -> int: ...
    def getUserId(self) -> int: ...
    def isAppGroup(self) -> bool: ...
    def isClearable(self) -> bool: ...
    def isGroup(self) -> bool: ...
    def isOngoing(self) -> bool: ...
    def setOverrideGroupKey(self, p0: str) -> None: ...
    def toString(self) -> str: ...
    @overload
    def clone(self) -> "StatusBarNotification": ...
    @overload
    def clone(self) -> Any: ...
    def getPackageName(self) -> str: ...
    def getKey(self) -> str: ...
    def getId(self) -> int: ...
    def getTag(self) -> str: ...
    def getUser(self) -> UserHandle: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getUid(self) -> int: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class ZenPolicy:
    CONVERSATION_SENDERS_ANYONE: ClassVar[int]
    CONVERSATION_SENDERS_IMPORTANT: ClassVar[int]
    CONVERSATION_SENDERS_NONE: ClassVar[int]
    CONVERSATION_SENDERS_UNSET: ClassVar[int]
    CREATOR: ClassVar[Any]
    PEOPLE_TYPE_ANYONE: ClassVar[int]
    PEOPLE_TYPE_CONTACTS: ClassVar[int]
    PEOPLE_TYPE_NONE: ClassVar[int]
    PEOPLE_TYPE_STARRED: ClassVar[int]
    PEOPLE_TYPE_UNSET: ClassVar[int]
    STATE_ALLOW: ClassVar[int]
    STATE_DISALLOW: ClassVar[int]
    STATE_UNSET: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getPriorityCallSenders(self) -> int: ...
    def getPriorityCategoryAlarms(self) -> int: ...
    def getPriorityCategoryCalls(self) -> int: ...
    def getPriorityCategoryConversations(self) -> int: ...
    def getPriorityCategoryEvents(self) -> int: ...
    def getPriorityCategoryMedia(self) -> int: ...
    def getPriorityCategoryMessages(self) -> int: ...
    def getPriorityCategoryReminders(self) -> int: ...
    def getPriorityCategoryRepeatCallers(self) -> int: ...
    def getPriorityCategorySystem(self) -> int: ...
    def getPriorityChannelsAllowed(self) -> int: ...
    def getPriorityConversationSenders(self) -> int: ...
    def getPriorityMessageSenders(self) -> int: ...
    def getVisualEffectAmbient(self) -> int: ...
    def getVisualEffectBadge(self) -> int: ...
    def getVisualEffectFullScreenIntent(self) -> int: ...
    def getVisualEffectLights(self) -> int: ...
    def getVisualEffectNotificationList(self) -> int: ...
    def getVisualEffectPeek(self) -> int: ...
    def getVisualEffectStatusBar(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self) -> None: ...
        def allowAllSounds(self) -> Any: ...
        def allowConversations(self, p0: int) -> Any: ...
        def allowEvents(self, p0: bool) -> Any: ...
        def allowMedia(self, p0: bool) -> Any: ...
        def showInAmbientDisplay(self, p0: bool) -> Any: ...
        def showInNotificationList(self, p0: bool) -> Any: ...
        def showLights(self, p0: bool) -> Any: ...
        def showPeeking(self, p0: bool) -> Any: ...
        def showStatusBarIcons(self, p0: bool) -> Any: ...
        def allowAlarms(self, p0: bool) -> Any: ...
        def allowCalls(self, p0: int) -> Any: ...
        def allowMessages(self, p0: int) -> Any: ...
        def allowPriorityChannels(self, p0: bool) -> Any: ...
        def allowReminders(self, p0: bool) -> Any: ...
        def allowRepeatCallers(self, p0: bool) -> Any: ...
        def allowSystem(self, p0: bool) -> Any: ...
        def disallowAllSounds(self) -> Any: ...
        def hideAllVisualEffects(self) -> Any: ...
        def showAllVisualEffects(self) -> Any: ...
        def showBadges(self, p0: bool) -> Any: ...
        def showFullScreenIntent(self, p0: bool) -> Any: ...
        def build(self) -> "ZenPolicy": ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.net.Uri import Uri
from android.os.Parcel import Parcel

class Condition:
    CREATOR: ClassVar[Any]
    FLAG_RELEVANT_ALWAYS: ClassVar[int]
    FLAG_RELEVANT_NOW: ClassVar[int]
    SCHEME: ClassVar[str]
    SOURCE_CONTEXT: ClassVar[int]
    SOURCE_SCHEDULE: ClassVar[int]
    SOURCE_UNKNOWN: ClassVar[int]
    SOURCE_USER_ACTION: ClassVar[int]
    STATE_ERROR: ClassVar[int]
    STATE_FALSE: ClassVar[int]
    STATE_TRUE: ClassVar[int]
    STATE_UNKNOWN: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    flags: int
    icon: int
    id: Uri
    line1: str
    line2: str
    source: int
    state: int
    summary: str
    @overload
    def __init__(self, p0: Uri, p1: str, p2: int) -> None: ...
    @overload
    def __init__(self, p0: Uri, p1: str, p2: int, p3: int) -> None: ...
    @overload
    def __init__(self, p0: Uri, p1: str, p2: str, p3: str, p4: int, p5: int, p6: int) -> None: ...
    @overload
    def __init__(self, p0: Uri, p1: str, p2: str, p3: str, p4: int, p5: int, p6: int, p7: int) -> None: ...
    @overload
    def __init__(self, p0: Parcel) -> None: ...
    @staticmethod
    def isValidId(p0: Uri, p1: str) -> bool: ...
    @staticmethod
    def stateToString(p0: int) -> str: ...
    @staticmethod
    def newId(p0: Context) -> Any: ...
    @staticmethod
    def relevanceToString(p0: int) -> str: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def copy(self) -> "Condition": ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class ZenDeviceEffects:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def shouldSuppressAmbientDisplay(self) -> bool: ...
    def shouldDimWallpaper(self) -> bool: ...
    def shouldUseNightMode(self) -> bool: ...
    def shouldDisplayGrayscale(self) -> bool: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        @overload
        def __init__(self, p0: "ZenDeviceEffects") -> None: ...
        @overload
        def __init__(self) -> None: ...
        def setShouldDimWallpaper(self, p0: bool) -> Any: ...
        def setShouldDisplayGrayscale(self, p0: bool) -> Any: ...
        def setShouldSuppressAmbientDisplay(self, p0: bool) -> Any: ...
        def setShouldUseNightMode(self, p0: bool) -> Any: ...
        def build(self) -> "ZenDeviceEffects": ...

from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Intent import Intent
from android.net.Uri import Uri
from android.os.IBinder import IBinder
from android.service.notification.Condition import Condition

class ConditionProviderService:
    EXTRA_RULE_ID: ClassVar[str]
    META_DATA_CONFIGURATION_ACTIVITY: ClassVar[str]
    META_DATA_RULE_INSTANCE_LIMIT: ClassVar[str]
    META_DATA_RULE_TYPE: ClassVar[str]
    SERVICE_INTERFACE: ClassVar[str]
    START_CONTINUATION_MASK: ClassVar[int]
    START_FLAG_REDELIVERY: ClassVar[int]
    START_FLAG_RETRY: ClassVar[int]
    START_NOT_STICKY: ClassVar[int]
    START_REDELIVER_INTENT: ClassVar[int]
    START_STICKY: ClassVar[int]
    START_STICKY_COMPATIBILITY: ClassVar[int]
    STOP_FOREGROUND_DETACH: ClassVar[int]
    STOP_FOREGROUND_LEGACY: ClassVar[int]
    STOP_FOREGROUND_REMOVE: ClassVar[int]
    TRIM_MEMORY_BACKGROUND: ClassVar[int]
    TRIM_MEMORY_COMPLETE: ClassVar[int]
    TRIM_MEMORY_MODERATE: ClassVar[int]
    TRIM_MEMORY_RUNNING_CRITICAL: ClassVar[int]
    TRIM_MEMORY_RUNNING_LOW: ClassVar[int]
    TRIM_MEMORY_RUNNING_MODERATE: ClassVar[int]
    TRIM_MEMORY_UI_HIDDEN: ClassVar[int]
    ACCESSIBILITY_SERVICE: ClassVar[str]
    ACCOUNT_SERVICE: ClassVar[str]
    ACTIVITY_SERVICE: ClassVar[str]
    ADVANCED_PROTECTION_SERVICE: ClassVar[str]
    ALARM_SERVICE: ClassVar[str]
    APPWIDGET_SERVICE: ClassVar[str]
    APP_FUNCTION_SERVICE: ClassVar[str]
    APP_OPS_SERVICE: ClassVar[str]
    APP_SEARCH_SERVICE: ClassVar[str]
    AUDIO_SERVICE: ClassVar[str]
    BATTERY_SERVICE: ClassVar[str]
    BIND_ABOVE_CLIENT: ClassVar[int]
    BIND_ADJUST_WITH_ACTIVITY: ClassVar[int]
    BIND_ALLOW_ACTIVITY_STARTS: ClassVar[int]
    BIND_ALLOW_OOM_MANAGEMENT: ClassVar[int]
    BIND_AUTO_CREATE: ClassVar[int]
    BIND_DEBUG_UNBIND: ClassVar[int]
    BIND_EXTERNAL_SERVICE: ClassVar[int]
    BIND_EXTERNAL_SERVICE_LONG: ClassVar[int]
    BIND_IMPORTANT: ClassVar[int]
    BIND_INCLUDE_CAPABILITIES: ClassVar[int]
    BIND_NOT_FOREGROUND: ClassVar[int]
    BIND_NOT_PERCEPTIBLE: ClassVar[int]
    BIND_PACKAGE_ISOLATED_PROCESS: ClassVar[int]
    BIND_SHARED_ISOLATED_PROCESS: ClassVar[int]
    BIND_WAIVE_PRIORITY: ClassVar[int]
    BIOMETRIC_SERVICE: ClassVar[str]
    BLOB_STORE_SERVICE: ClassVar[str]
    BLUETOOTH_SERVICE: ClassVar[str]
    BUGREPORT_SERVICE: ClassVar[str]
    CAMERA_SERVICE: ClassVar[str]
    CAPTIONING_SERVICE: ClassVar[str]
    CARRIER_CONFIG_SERVICE: ClassVar[str]
    CLIPBOARD_SERVICE: ClassVar[str]
    COMPANION_DEVICE_SERVICE: ClassVar[str]
    CONNECTIVITY_DIAGNOSTICS_SERVICE: ClassVar[str]
    CONNECTIVITY_SERVICE: ClassVar[str]
    CONSUMER_IR_SERVICE: ClassVar[str]
    CONTACT_KEYS_SERVICE: ClassVar[str]
    CONTEXT_IGNORE_SECURITY: ClassVar[int]
    CONTEXT_INCLUDE_CODE: ClassVar[int]
    CONTEXT_RESTRICTED: ClassVar[int]
    CREDENTIAL_SERVICE: ClassVar[str]
    CROSS_PROFILE_APPS_SERVICE: ClassVar[str]
    DEVICE_ID_DEFAULT: ClassVar[int]
    DEVICE_ID_INVALID: ClassVar[int]
    DEVICE_LOCK_SERVICE: ClassVar[str]
    DEVICE_POLICY_SERVICE: ClassVar[str]
    DISPLAY_HASH_SERVICE: ClassVar[str]
    DISPLAY_SERVICE: ClassVar[str]
    DOMAIN_VERIFICATION_SERVICE: ClassVar[str]
    DOWNLOAD_SERVICE: ClassVar[str]
    DROPBOX_SERVICE: ClassVar[str]
    EUICC_SERVICE: ClassVar[str]
    FILE_INTEGRITY_SERVICE: ClassVar[str]
    FINGERPRINT_SERVICE: ClassVar[str]
    GAME_SERVICE: ClassVar[str]
    GRAMMATICAL_INFLECTION_SERVICE: ClassVar[str]
    HARDWARE_PROPERTIES_SERVICE: ClassVar[str]
    HEALTHCONNECT_SERVICE: ClassVar[str]
    INPUT_METHOD_SERVICE: ClassVar[str]
    INPUT_SERVICE: ClassVar[str]
    IPSEC_SERVICE: ClassVar[str]
    JOB_SCHEDULER_SERVICE: ClassVar[str]
    KEYGUARD_SERVICE: ClassVar[str]
    KEYSTORE_SERVICE: ClassVar[str]
    LAUNCHER_APPS_SERVICE: ClassVar[str]
    LAYOUT_INFLATER_SERVICE: ClassVar[str]
    LOCALE_SERVICE: ClassVar[str]
    LOCATION_SERVICE: ClassVar[str]
    MEDIA_COMMUNICATION_SERVICE: ClassVar[str]
    MEDIA_METRICS_SERVICE: ClassVar[str]
    MEDIA_PROJECTION_SERVICE: ClassVar[str]
    MEDIA_QUALITY_SERVICE: ClassVar[str]
    MEDIA_ROUTER_SERVICE: ClassVar[str]
    MEDIA_SESSION_SERVICE: ClassVar[str]
    MIDI_SERVICE: ClassVar[str]
    MODE_APPEND: ClassVar[int]
    MODE_ENABLE_WRITE_AHEAD_LOGGING: ClassVar[int]
    MODE_MULTI_PROCESS: ClassVar[int]
    MODE_NO_LOCALIZED_COLLATORS: ClassVar[int]
    MODE_PRIVATE: ClassVar[int]
    MODE_WORLD_READABLE: ClassVar[int]
    MODE_WORLD_WRITEABLE: ClassVar[int]
    NETWORK_STATS_SERVICE: ClassVar[str]
    NFC_SERVICE: ClassVar[str]
    NOTIFICATION_SERVICE: ClassVar[str]
    NSD_SERVICE: ClassVar[str]
    OVERLAY_SERVICE: ClassVar[str]
    PEOPLE_SERVICE: ClassVar[str]
    PERFORMANCE_HINT_SERVICE: ClassVar[str]
    PERSISTENT_DATA_BLOCK_SERVICE: ClassVar[str]
    POWER_SERVICE: ClassVar[str]
    PRINT_SERVICE: ClassVar[str]
    PROFILING_SERVICE: ClassVar[str]
    RECEIVER_EXPORTED: ClassVar[int]
    RECEIVER_NOT_EXPORTED: ClassVar[int]
    RECEIVER_VISIBLE_TO_INSTANT_APPS: ClassVar[int]
    RESTRICTIONS_SERVICE: ClassVar[str]
    ROLE_SERVICE: ClassVar[str]
    SATELLITE_SERVICE: ClassVar[str]
    SEARCH_SERVICE: ClassVar[str]
    SECURITY_STATE_SERVICE: ClassVar[str]
    SENSOR_SERVICE: ClassVar[str]
    SHORTCUT_SERVICE: ClassVar[str]
    STATUS_BAR_SERVICE: ClassVar[str]
    STORAGE_SERVICE: ClassVar[str]
    STORAGE_STATS_SERVICE: ClassVar[str]
    SYSTEM_HEALTH_SERVICE: ClassVar[str]
    TELECOM_SERVICE: ClassVar[str]
    TELEPHONY_IMS_SERVICE: ClassVar[str]
    TELEPHONY_SERVICE: ClassVar[str]
    TELEPHONY_SUBSCRIPTION_SERVICE: ClassVar[str]
    TETHERING_SERVICE: ClassVar[str]
    TEXT_CLASSIFICATION_SERVICE: ClassVar[str]
    TEXT_SERVICES_MANAGER_SERVICE: ClassVar[str]
    TV_AD_SERVICE: ClassVar[str]
    TV_INPUT_SERVICE: ClassVar[str]
    TV_INTERACTIVE_APP_SERVICE: ClassVar[str]
    UI_MODE_SERVICE: ClassVar[str]
    USAGE_STATS_SERVICE: ClassVar[str]
    USB_SERVICE: ClassVar[str]
    USER_SERVICE: ClassVar[str]
    VIBRATOR_MANAGER_SERVICE: ClassVar[str]
    VIBRATOR_SERVICE: ClassVar[str]
    VIRTUAL_DEVICE_SERVICE: ClassVar[str]
    VPN_MANAGEMENT_SERVICE: ClassVar[str]
    WALLPAPER_SERVICE: ClassVar[str]
    WIFI_AWARE_SERVICE: ClassVar[str]
    WIFI_P2P_SERVICE: ClassVar[str]
    WIFI_RTT_RANGING_SERVICE: ClassVar[str]
    WIFI_SERVICE: ClassVar[str]
    WINDOW_SERVICE: ClassVar[str]
    def __init__(self) -> None: ...
    def notifyCondition(self, p0: Condition) -> None: ...
    def notifyConditions(self, p0: Any) -> None: ...
    def onConnected(self) -> None: ...
    def onRequestConditions(self, p0: int) -> None: ...
    def onSubscribe(self, p0: Uri) -> None: ...
    def onUnsubscribe(self, p0: Uri) -> None: ...
    @staticmethod
    def requestRebind(p0: ComponentName) -> None: ...
    def requestUnbind(self) -> None: ...
    def onBind(self, p0: Intent) -> IBinder: ...

