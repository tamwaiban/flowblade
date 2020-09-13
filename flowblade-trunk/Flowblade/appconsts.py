"""
    Flowblade Movie Editor is a nonlinear video editor.
    Copyright 2012 Janne Liljeblad.

    This file is part of Flowblade Movie Editor <http://code.google.com/p/flowblade>.

    Flowblade Movie Editor is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Flowblade Movie Editor is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Flowblade Movie Editor.  If not, see <http://www.gnu.org/licenses/>.
"""

"""
Module contains constant values that are used by multiple modules in the application. 
"""

PROJECT_FILE_EXTENSION = ".flb"

# Media types for tracks or clips
UNKNOWN = 0
VIDEO = 1
AUDIO = 2
IMAGE = 3
RENDERED_VIDEO = 4 # not used
PATTERN_PRODUCER = 5
SYNC_AUDIO = 6
FILE_DOES_NOT_EXIST = 7
IMAGE_SEQUENCE = 8

# Media view filtering options
SHOW_ALL_FILES = 0
SHOW_VIDEO_FILES = 1
SHOW_AUDIO_FILES = 2
SHOW_GRAPHICS_FILES = 3
SHOW_IMAGE_SEQUENCES = 4
SHOW_PATTERN_PRODUCERS = 5
SHOW_UNUSED_FILES = 6

# These are used to draw indicators that tell if more frames are available while trimming
ON_FIRST_FRAME = 0
ON_LAST_FRAME = 1
ON_BETWEEN_FRAME = 2

# Sync states of sync child clips
SYNC_CORRECT = 0
SYNC_OFF = 1
SYNC_PARENT_GONE = 2

# Allowed editing operations on a track
FREE = 0        # All edits allowed
SYNC_LOCKED = 1 # No insert, splice out or one roll trim.
                # Allowed edits do not change positions of later clips 
LOCKED = 2      # No edits allowed

# Property types of mlt filters and mlt transitions in filters.xml
# and compositors.xml
PROP_INT = 0
PROP_FLOAT = 1
PROP_EXPRESSION = 2

# Display heights for tracks and timeline.
TRACK_HEIGHT_HIGH = 75 # track height in canvas and column
TRACK_HEIGHT_NORMAL = 50 # track height in canvas and column
TRACK_HEIGHT_SMALL = 25  # track height in canvas and column
TRACK_HEIGHT_SMALLEST = 25 # maybe remove this as it is no longer used
TLINE_HEIGHT = 260

# Notebook widths
NOTEBOOK_WIDTH = 600 # defines app min width together with MONITOR_AREA_WIDTH
NOTEBOOK_WIDTH_WIDESCREEN = 500
TOP_ROW_HEIGHT = 500

# Property editing gui consts
PROPERTY_ROW_HEIGHT = 22
PROPERTY_NAME_WIDTH = 90

# Clip mute options
MUTE_NOTHING = 0
MUTE_AUDIO = 1
MUTE_VIDEO = 2
MUTE_ALL = 3

# Track mute options
TRACK_MUTE_NOTHING = 0
TRACK_MUTE_VIDEO = 1
TRACK_MUTE_AUDIO = 2
TRACK_MUTE_ALL = 3

# XML Attribute and element names used in multiple modules
NAME = "name"
ARGS = "args"
PROPERTY = "property"
NON_MLT_PROPERTY = "propertynonmlt"
MLT_SERVICE = "mlt_service"
EXTRA_EDITOR = "extraeditor"

# Available tracks maximum for Flowblade
MAX_TRACKS = 9
INIT_V_TRACKS = 5
INIT_A_TRACKS = 4

# Thumbnail image dimensions
THUMB_WIDTH = 116
THUMB_HEIGHT = 87

# Magic value for no pan being applied for audio producer
NO_PAN = -99

# Copy of projectdata.SAVEFILE_VERSION is here to be available at savetime without importing projectdata
# This is set at application startup in app.main()
SAVEFILE_VERSION = -1

# This color is used in two modules
MIDBAR_COLOR = "#bdbdbd"

# Media log event types
MEDIA_LOG_ALL = -1 # no MediaLogEvent has this type, this is used when filtering events for display
MEDIA_LOG_INSERT = 0
MEDIA_LOG_MARKS_SET = 1

# Media log item sorting
TIME_SORT = 0
NAME_SORT = 1
COMMENT_SORT = 2

# Rendered clip types
RENDERED_DISSOLVE = 0
RENDERED_WIPE = 1
RENDERED_COLOR_DIP = 2
RENDERED_FADE_IN = 3
RENDERED_FADE_OUT = 4

# Project proxy modes
USE_ORIGINAL_MEDIA = 0
USE_PROXY_MEDIA = 1
CONVERTING_TO_USE_PROXY_MEDIA = 2
CONVERTING_TO_USE_ORIGINAL_MEDIA = 3

# Autosave directory relative path
AUTOSAVE_DIR = "autosave/"

# Hidden media folders
# NOTE: We have not been fully consistant with the ending forward slashes.
AUDIO_LEVELS_DIR = "audiolevels/"
PROXIES_DIR = "proxies/"
THUMBNAILS_DIR = "thumbnails"
RENDERED_CLIPS_DIR = "rendered_clips"
TLINE_RENDERS_DIR = "tlinerenders"
GMIC_DIR = "gmic"
PHANTOM_DIR = "phantom2d"
PHANTOM_DISK_CACHE_DIR = "disk_cache"
MATCH_FRAME_DIR = "match_frame"
MATCH_FRAME = MATCH_FRAME_DIR + "/match_frame.png"
MATCH_FRAME_NEW = MATCH_FRAME_DIR + "/match_frame_new.png"
TRIM_VIEW_DIR = "trim_view"
USER_PROFILES_DIR = "user_profiles/"
USER_PROFILES_DIR_NO_SLASH = "user_profiles"
BATCH_DIR = "batchrender/"
CONTAINER_CLIPS_DIR = "container_clips"
CONTAINER_CLIPS_UNRENDERED = "container_clips/unrendered"
CC_CLIP_FRAMES_DIR = "/clip_frames"
CC_RENDERED_FRAMES_DIR = "/rendered_frames"
CC_PREVIEW_RENDER_DIR = "/preview_frames"
USER_SHORTCUTS_DIR =  "user_shortcuts/"

# Luma bands
SHADOWS = 0
MIDTONES = 1
HIGHLIGHTS = 2

# Multi move edit ops
MULTI_NOOP = 0
MULTI_ADD_TRIM = 1
MULTI_TRIM_REMOVE = 2
MULTI_TRIM = 3

# Jack options (not used currently)
JACK_ON_START_UP_NO = 0
JACK_ON_START_UP_YES = 1
JACK_OUT_AUDIO = 0
JACK_OUT_SYNC = 0

# Media load order options
LOAD_ABSOLUTE_FIRST = 0
LOAD_RELATIVE_FIRST = 1
LOAD_ABSOLUTE_ONLY = 2

# Trim view modes
TRIM_VIEW_ON = 0
TRIM_VIEW_SINGLE = 1
TRIM_VIEW_OFF = 2

# Midbar layout
MIDBAR_TC_LEFT = 0
MIDBAR_TC_CENTER = 1
MIDBAR_COMPONENTS_CENTERED = 2
MIDBAR_TC_FREE = 3

# Windows mode
SINGLE_WINDOW = 1
TWO_WINDOWS = 2

# Apr-2017 - SvdB
SHORTCUTS_DEFAULT = 'Flowblade Default'
SHORTCUTS_DEFAULT_XML = 'flowblade'
SHORTCUTS_ROOT_TAG = 'flowblade'
SHORTCUTS_TAG = 'shortcuts'

# Project properties keys
P_PROP_TLINE_SHRINK_VERTICAL = "tline_shrink_vertical"
P_PROP_LAST_RENDER_SELECTIONS = "P_PROP_LAST_RENDER_SELECTIONS"
P_PROP_TRANSITION_ENCODING = "P_PROP_TRANSITION_ENCODING"
P_PROP_DEFAULT_FADE_LENGTH = "P_PROP_DEFAULT_FADE_LENGTH"

# A context defining action taken when mouse press happens based on edit mode ands mouse position
POINTER_CONTEXT_NONE = 0
POINTER_CONTEXT_END_DRAG_LEFT = 1
POINTER_CONTEXT_END_DRAG_RIGHT = 2
POINTER_CONTEXT_COMPOSITOR_MOVE = 3
POINTER_CONTEXT_COMPOSITOR_END_DRAG_LEFT = 4
POINTER_CONTEXT_COMPOSITOR_END_DRAG_RIGHT = 5
POINTER_CONTEXT_TRIM_LEFT = 6
POINTER_CONTEXT_TRIM_RIGHT = 7
POINTER_CONTEXT_BOX_SIDEWAYS = 8
POINTER_CONTEXT_MULTI_ROLL = 9
POINTER_CONTEXT_MULTI_SLIP = 10

# Timeline tool ids. NOTE: a tool can map to 1 or more editmodes and even module specified submodes, depending on complexity of edit actions.
TLINE_TOOL_INSERT = 1
TLINE_TOOL_OVERWRITE = 2
TLINE_TOOL_TRIM = 3
TLINE_TOOL_ROLL = 4
TLINE_TOOL_SLIP = 5
TLINE_TOOL_SPACER = 6
TLINE_TOOL_BOX = 7
TLINE_TOOL_RIPPLE_TRIM = 8
TLINE_TOOL_CUT = 9
TLINE_TOOL_KFTOOL = 10
TLINE_TOOL_MULTI_TRIM = 11

# Monitor switch events
MONITOR_TLINE_BUTTON_PRESSED = 1
MONITOR_CLIP_BUTTON_PRESSED = 2

# Appliation thmes and colors preference
FLOWBLADE_THEME = 0
DARK_THEME = 1
LIGHT_THEME = 2

# DND actions
DND_ALWAYS_OVERWRITE = 0
DND_OVERWRITE_NON_V1 = 1
DND_ALWAYS_INSERT = 2

# Top row layouts
THREE_PANELS_IF_POSSIBLE = 0
ALWAYS_TWO_PANELS = 1

# Copypaste data tyoe
COPY_PASTE_DATA_CLIPS = 1
COPY_PASTE_DATA_COMPOSITOR_PROPERTIES = 2
COPY_PASTE_KEYFRAME_EDITOR_KF_DATA = 3
COPY_PASTE_GEOMETRY_EDITOR_KF_DATA = 4

# Timeline Compositong modes
COMPOSITING_MODE_TOP_DOWN_FREE_MOVE = 0
COMPOSITING_MODE_TOP_DOWN_AUTO_FOLLOW = 1 # Deprecated, mode removed 2.6 ->
COMPOSITING_MODE_STANDARD_AUTO_FOLLOW = 2
COMPOSITING_MODE_STANDARD_FULL_TRACK = 3

# Magic string for selection path being user home directory root
USER_HOME_DIR = "USER_HOME_DIERCTORY_&&##&&"

# Timeline rendering modes
TLINE_RENDERING_OFF = 0
TLINE_RENDERING_AUTO = 1
TLINE_RENDERING_REQUEST = 2

# Timeline rendering uses these now
PROXY_SIZE_FULL = 0
PROXY_SIZE_HALF = 1
PROXY_SIZE_QUARTER = 2


# Container clip types
CONTAINER_CLIP_GMIC = 0
CONTAINER_CLIP_MLT_XML = 1
CONTAINER_CLIP_CAIRO_SCRIPT = 2
CONTAINER_CLIP_BLENDER = 3

CONTAINER_CLIP_VIDEO_CLIP_NAME = "container_clip"

# Middlebar GUI objects
BUTTON_GROUP_TOOLS = "tool_buttons"
BUTTON_GROUP_UNDO = "undo_redo"
BUTTON_GROUP_ZOOM = "zoom_buttons"
BUTTON_GROUP_EDIT =  "edit_buttons"
BUTTON_GROUP_SYNC_SPLIT = "edit_buttons_2"
BUTTON_GROUP_DELETE = "edit_buttons_3"
BUTTON_GROUP_MONITOR_ADD = "monitor_insert_buttons"
BIG_TIME_CODE = "big_TC"
WORKFLOW_LAUNCH = "worflow_launch" 
TOOL_SELECT = "tool_selector"

