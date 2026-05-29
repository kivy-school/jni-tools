from typing import Any, ClassVar, overload
from android.graphics.Bitmap import Bitmap
from java.io.File import File
from java.io.FileDescriptor import FileDescriptor
from java.io.InputStream import InputStream

class ExifInterface:
    ORIENTATION_FLIP_HORIZONTAL: ClassVar[int]
    ORIENTATION_FLIP_VERTICAL: ClassVar[int]
    ORIENTATION_NORMAL: ClassVar[int]
    ORIENTATION_ROTATE_180: ClassVar[int]
    ORIENTATION_ROTATE_270: ClassVar[int]
    ORIENTATION_ROTATE_90: ClassVar[int]
    ORIENTATION_TRANSPOSE: ClassVar[int]
    ORIENTATION_TRANSVERSE: ClassVar[int]
    ORIENTATION_UNDEFINED: ClassVar[int]
    STREAM_TYPE_EXIF_DATA_ONLY: ClassVar[int]
    STREAM_TYPE_FULL_IMAGE_DATA: ClassVar[int]
    TAG_APERTURE: ClassVar[str]
    TAG_APERTURE_VALUE: ClassVar[str]
    TAG_ARTIST: ClassVar[str]
    TAG_BITS_PER_SAMPLE: ClassVar[str]
    TAG_BRIGHTNESS_VALUE: ClassVar[str]
    TAG_CFA_PATTERN: ClassVar[str]
    TAG_COLOR_SPACE: ClassVar[str]
    TAG_COMPONENTS_CONFIGURATION: ClassVar[str]
    TAG_COMPRESSED_BITS_PER_PIXEL: ClassVar[str]
    TAG_COMPRESSION: ClassVar[str]
    TAG_CONTRAST: ClassVar[str]
    TAG_COPYRIGHT: ClassVar[str]
    TAG_CUSTOM_RENDERED: ClassVar[str]
    TAG_DATETIME: ClassVar[str]
    TAG_DATETIME_DIGITIZED: ClassVar[str]
    TAG_DATETIME_ORIGINAL: ClassVar[str]
    TAG_DEFAULT_CROP_SIZE: ClassVar[str]
    TAG_DEVICE_SETTING_DESCRIPTION: ClassVar[str]
    TAG_DIGITAL_ZOOM_RATIO: ClassVar[str]
    TAG_DNG_VERSION: ClassVar[str]
    TAG_EXIF_VERSION: ClassVar[str]
    TAG_EXPOSURE_BIAS_VALUE: ClassVar[str]
    TAG_EXPOSURE_INDEX: ClassVar[str]
    TAG_EXPOSURE_MODE: ClassVar[str]
    TAG_EXPOSURE_PROGRAM: ClassVar[str]
    TAG_EXPOSURE_TIME: ClassVar[str]
    TAG_FILE_SOURCE: ClassVar[str]
    TAG_FLASH: ClassVar[str]
    TAG_FLASHPIX_VERSION: ClassVar[str]
    TAG_FLASH_ENERGY: ClassVar[str]
    TAG_FOCAL_LENGTH: ClassVar[str]
    TAG_FOCAL_LENGTH_IN_35MM_FILM: ClassVar[str]
    TAG_FOCAL_PLANE_RESOLUTION_UNIT: ClassVar[str]
    TAG_FOCAL_PLANE_X_RESOLUTION: ClassVar[str]
    TAG_FOCAL_PLANE_Y_RESOLUTION: ClassVar[str]
    TAG_F_NUMBER: ClassVar[str]
    TAG_GAIN_CONTROL: ClassVar[str]
    TAG_GPS_ALTITUDE: ClassVar[str]
    TAG_GPS_ALTITUDE_REF: ClassVar[str]
    TAG_GPS_AREA_INFORMATION: ClassVar[str]
    TAG_GPS_DATESTAMP: ClassVar[str]
    TAG_GPS_DEST_BEARING: ClassVar[str]
    TAG_GPS_DEST_BEARING_REF: ClassVar[str]
    TAG_GPS_DEST_DISTANCE: ClassVar[str]
    TAG_GPS_DEST_DISTANCE_REF: ClassVar[str]
    TAG_GPS_DEST_LATITUDE: ClassVar[str]
    TAG_GPS_DEST_LATITUDE_REF: ClassVar[str]
    TAG_GPS_DEST_LONGITUDE: ClassVar[str]
    TAG_GPS_DEST_LONGITUDE_REF: ClassVar[str]
    TAG_GPS_DIFFERENTIAL: ClassVar[str]
    TAG_GPS_DOP: ClassVar[str]
    TAG_GPS_IMG_DIRECTION: ClassVar[str]
    TAG_GPS_IMG_DIRECTION_REF: ClassVar[str]
    TAG_GPS_LATITUDE: ClassVar[str]
    TAG_GPS_LATITUDE_REF: ClassVar[str]
    TAG_GPS_LONGITUDE: ClassVar[str]
    TAG_GPS_LONGITUDE_REF: ClassVar[str]
    TAG_GPS_MAP_DATUM: ClassVar[str]
    TAG_GPS_MEASURE_MODE: ClassVar[str]
    TAG_GPS_PROCESSING_METHOD: ClassVar[str]
    TAG_GPS_SATELLITES: ClassVar[str]
    TAG_GPS_SPEED: ClassVar[str]
    TAG_GPS_SPEED_REF: ClassVar[str]
    TAG_GPS_STATUS: ClassVar[str]
    TAG_GPS_TIMESTAMP: ClassVar[str]
    TAG_GPS_TRACK: ClassVar[str]
    TAG_GPS_TRACK_REF: ClassVar[str]
    TAG_GPS_VERSION_ID: ClassVar[str]
    TAG_IMAGE_DESCRIPTION: ClassVar[str]
    TAG_IMAGE_LENGTH: ClassVar[str]
    TAG_IMAGE_UNIQUE_ID: ClassVar[str]
    TAG_IMAGE_WIDTH: ClassVar[str]
    TAG_INTEROPERABILITY_INDEX: ClassVar[str]
    TAG_ISO: ClassVar[str]
    TAG_ISO_SPEED_RATINGS: ClassVar[str]
    TAG_JPEG_INTERCHANGE_FORMAT: ClassVar[str]
    TAG_JPEG_INTERCHANGE_FORMAT_LENGTH: ClassVar[str]
    TAG_LIGHT_SOURCE: ClassVar[str]
    TAG_MAKE: ClassVar[str]
    TAG_MAKER_NOTE: ClassVar[str]
    TAG_MAX_APERTURE_VALUE: ClassVar[str]
    TAG_METERING_MODE: ClassVar[str]
    TAG_MODEL: ClassVar[str]
    TAG_NEW_SUBFILE_TYPE: ClassVar[str]
    TAG_OECF: ClassVar[str]
    TAG_OFFSET_TIME: ClassVar[str]
    TAG_OFFSET_TIME_DIGITIZED: ClassVar[str]
    TAG_OFFSET_TIME_ORIGINAL: ClassVar[str]
    TAG_ORF_ASPECT_FRAME: ClassVar[str]
    TAG_ORF_PREVIEW_IMAGE_LENGTH: ClassVar[str]
    TAG_ORF_PREVIEW_IMAGE_START: ClassVar[str]
    TAG_ORF_THUMBNAIL_IMAGE: ClassVar[str]
    TAG_ORIENTATION: ClassVar[str]
    TAG_PHOTOMETRIC_INTERPRETATION: ClassVar[str]
    TAG_PIXEL_X_DIMENSION: ClassVar[str]
    TAG_PIXEL_Y_DIMENSION: ClassVar[str]
    TAG_PLANAR_CONFIGURATION: ClassVar[str]
    TAG_PRIMARY_CHROMATICITIES: ClassVar[str]
    TAG_REFERENCE_BLACK_WHITE: ClassVar[str]
    TAG_RELATED_SOUND_FILE: ClassVar[str]
    TAG_RESOLUTION_UNIT: ClassVar[str]
    TAG_ROWS_PER_STRIP: ClassVar[str]
    TAG_RW2_ISO: ClassVar[str]
    TAG_RW2_JPG_FROM_RAW: ClassVar[str]
    TAG_RW2_SENSOR_BOTTOM_BORDER: ClassVar[str]
    TAG_RW2_SENSOR_LEFT_BORDER: ClassVar[str]
    TAG_RW2_SENSOR_RIGHT_BORDER: ClassVar[str]
    TAG_RW2_SENSOR_TOP_BORDER: ClassVar[str]
    TAG_SAMPLES_PER_PIXEL: ClassVar[str]
    TAG_SATURATION: ClassVar[str]
    TAG_SCENE_CAPTURE_TYPE: ClassVar[str]
    TAG_SCENE_TYPE: ClassVar[str]
    TAG_SENSING_METHOD: ClassVar[str]
    TAG_SHARPNESS: ClassVar[str]
    TAG_SHUTTER_SPEED_VALUE: ClassVar[str]
    TAG_SOFTWARE: ClassVar[str]
    TAG_SPATIAL_FREQUENCY_RESPONSE: ClassVar[str]
    TAG_SPECTRAL_SENSITIVITY: ClassVar[str]
    TAG_STRIP_BYTE_COUNTS: ClassVar[str]
    TAG_STRIP_OFFSETS: ClassVar[str]
    TAG_SUBFILE_TYPE: ClassVar[str]
    TAG_SUBJECT_AREA: ClassVar[str]
    TAG_SUBJECT_DISTANCE: ClassVar[str]
    TAG_SUBJECT_DISTANCE_RANGE: ClassVar[str]
    TAG_SUBJECT_LOCATION: ClassVar[str]
    TAG_SUBSEC_TIME: ClassVar[str]
    TAG_SUBSEC_TIME_DIG: ClassVar[str]
    TAG_SUBSEC_TIME_DIGITIZED: ClassVar[str]
    TAG_SUBSEC_TIME_ORIG: ClassVar[str]
    TAG_SUBSEC_TIME_ORIGINAL: ClassVar[str]
    TAG_THUMBNAIL_IMAGE_LENGTH: ClassVar[str]
    TAG_THUMBNAIL_IMAGE_WIDTH: ClassVar[str]
    TAG_THUMBNAIL_ORIENTATION: ClassVar[str]
    TAG_TRANSFER_FUNCTION: ClassVar[str]
    TAG_USER_COMMENT: ClassVar[str]
    TAG_WHITE_BALANCE: ClassVar[str]
    TAG_WHITE_POINT: ClassVar[str]
    TAG_XMP: ClassVar[str]
    TAG_X_RESOLUTION: ClassVar[str]
    TAG_Y_CB_CR_COEFFICIENTS: ClassVar[str]
    TAG_Y_CB_CR_POSITIONING: ClassVar[str]
    TAG_Y_CB_CR_SUB_SAMPLING: ClassVar[str]
    TAG_Y_RESOLUTION: ClassVar[str]
    WHITEBALANCE_AUTO: ClassVar[int]
    WHITEBALANCE_MANUAL: ClassVar[int]
    @overload
    def __init__(self, p0: File) -> None: ...
    @overload
    def __init__(self, p0: InputStream) -> None: ...
    @overload
    def __init__(self, p0: FileDescriptor) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: InputStream, p1: int) -> None: ...
    @staticmethod
    def isSupportedMimeType(p0: str) -> bool: ...
    def getAttributeInt(self, p0: str, p1: int) -> int: ...
    def getAttributeDouble(self, p0: str, p1: float) -> float: ...
    def saveAttributes(self) -> None: ...
    def hasThumbnail(self) -> bool: ...
    def hasAttribute(self, p0: str) -> bool: ...
    def getThumbnailBytes(self) -> Any: ...
    def getThumbnailBitmap(self) -> Bitmap: ...
    def isThumbnailCompressed(self) -> bool: ...
    def getThumbnailRange(self) -> Any: ...
    def getAttributeRange(self, p0: str) -> Any: ...
    def getAttributeBytes(self, p0: str) -> Any: ...
    def getLatLong(self, p0: Any) -> bool: ...
    def getDateTime(self) -> int: ...
    def getDateTimeDigitized(self) -> int: ...
    def getDateTimeOriginal(self) -> int: ...
    def getGpsDateTime(self) -> int: ...
    def getThumbnail(self) -> Any: ...
    def getAttribute(self, p0: str) -> str: ...
    def setAttribute(self, p0: str, p1: str) -> None: ...
    def getAltitude(self, p0: float) -> float: ...
