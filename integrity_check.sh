#!/bin/bash

TARGET_PATH="$1"

escape_for_sed() {
  echo $1 | sed 's/\//\\\//g'
}

while IFS='' read -r -d '' SOURCE_FILE; do
  ESCAPED_TARGET_PATH="$(escape_for_sed "$TARGET_PATH")"
  ESCAPED_TARGET_FILE="$(echo "$SOURCE_FILE" | sed "s/MOONCLOCK/$ESCAPED_TARGET_PATH/g")"

  if [[ -f "$ESCAPED_TARGET_FILE" ]]; then
    SOURCE_FILE_CHECKSUM="$(md5sum $SOURCE_FILE | awk '{ print $1 }')"
    TARGET_FILE_CHECKSUM="$(md5sum $ESCAPED_TARGET_FILE | awk '{ print $1 }')"

    if [[ "$SOURCE_FILE_CHECKSUM" == "$TARGET_FILE_CHECKSUM" ]]; then
      printf "OK \t %s\n" "$SOURCE_FILE"
    else
      printf "ERROR \t %s\n" "$SOURCE_FILE"
    fi
  else
    echo "File $SOURCE_FILE does not exist!"
  fi

done < <(find MOONCLOCK -type f -print0)
